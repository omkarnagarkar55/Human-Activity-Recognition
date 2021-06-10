

from flask import Flask, url_for, render_template, request, redirect, session ,Response
from flask_sqlalchemy import SQLAlchemy
from activityrecognition import Recognition


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, username, password):
        self.username = username
        self.password = password


rec = Recognition()

@app.route('/har')
def har(name=None ,methods=['GET']):
    if session.get('logged_in'):
        return render_template('home.html', name=name)
    else:
        return render_template('index.html', message="Please login to access!!!")


@app.route('/webcam')
def parse(name=None):
    #rec = Recognition()

    args = 0
    #rec.startrecognition(args)

    print("done2")
    return render_template('index2.html', name=name)


@app.route('/video')
def parse1(name=None):
    #rec = Recognition()

    args = 'wave.mp4'
    return Response(rec.startrecognition(args) , mimetype='multipart/x-mixed-replace; boundary=frame')

    #return render_template('index2.html', name=name)

@app.route('/', methods=['GET'])
def index():
    if session.get('logged_in'):
        return redirect(url_for('har'))
    else:
        return render_template('index.html', message="Welcome !!!")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            db.session.add(User(username=request.form['username'], password=request.form['password']))
            db.session.commit()
            return redirect(url_for('login'))
        except:
            return render_template('index.html', message="User Already Exists")
    else:
        return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        u = request.form['username']
        p = request.form['password']
        data = User.query.filter_by(username=u, password=p).first()
        if data is not None:
            session['logged_in'] = True
            return redirect(url_for('index'))
        return render_template('index.html', message="Incorrect Details")


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.secret_key = "ThisIsNotASecret:p"
    db.create_all()
    app.run(debug=True)
