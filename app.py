from flask import Flask, render_template
from activityrecognition import Recognition


app = Flask(__name__)

rec = Recognition()

@app.route('/')
def index(name=None):
    return render_template('index.html', name=name)

@app.route('/webcam')
def parse(name=None):
    #rec = Recognition()

    args = 0
    #rec.startrecognition(args)

    print("done2")
    return render_template('index.html', name=name)


@app.route('/video')
def parse1(name=None):
    #rec = Recognition()

    args = 'wave.mp4'
    rec.startrecognition(args)

    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
