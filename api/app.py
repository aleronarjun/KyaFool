import os
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')



APP_PATH = os.path.dirname(os.path.abspath(__file__));

@app.route('/upload', methods=['POST'])
def upload():
    target = os.path.join(APP_PATH, 'images/')
    print(target)
    print(request)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)

    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
