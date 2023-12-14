from flask import Flask, render_template, url_for, redirect,jsonify,make_response
from cloudipsp import Api, Checkout
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request,render_template, redirect,session
from flask_sqlalchemy import SQLAlchemy
import bcrypt
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.secret_key = 'secret_key'
api = Api(merchant_id=1396424,
          secret_key='test')


@app.route('/nsdap')
def nsdap():
    return render_template('nsdap.html')

@app.route('/makedonian_empire')
def makedonian_empire():
    return render_template('makedonian_empire.html')

@app.route('/mussolini')
def mussolini():
    return render_template('mussolini.html')

@app.route('/')
def wiki():
    return render_template('wiki.html')

@app.route('/napoleon')
def napoleon():
    return render_template('napoleon.html')

@app.route('/wikiuser')
def wikiuser():
    audio_files = ['/static/music.mp3', '/static/music1.mp3', '/static/music2.mp3','/static/music3.mp3','/static/music4.mp3','/static/music5.mp3','/static/music6.mp3','/static/music7.mp3','/static/music8.mp3','/static/music9.mp3','/static/music10.mp3','/static/music11.mp3','/static/music12.mp3','/static/music13.mp3','/static/music14.mp3','/static/music15.mp3','/static/music16.mp3','/static/music17.mp3','/static/music18.mp3','/static/music19.mp3','/static/music20.mp3','/static/music21.mp3','/static/music22.mp3','/static/music23.mp3']
    random_audio = random.choice(audio_files)
    if session['email']:
        user = User.query.filter_by(email=session['email']).first()
    return render_template('wikiuser.html',user=user,random_audio=random_audio)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/404')
def i404():
    return render_template('404.html')

@app.route('/card', methods=['GET', 'POST'])
def card():
    return render_template('card.html')


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self,email,password,name):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self,password):
        return bcrypt.checkpw(password.encode('utf-8'),self.password.encode('utf-8'))

with app.app_context():
    db.create_all()

@app.route('/me')
def me():
    return render_template('me.html')

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/commentaries')
def commentaries():
    return render_template('commentaries.html',)

@app.route('/napoleonwars')
def napoleonwars():
    return render_template('napoleonwars.html')


@app.route('/1618')
def sagaydachniy():
    return render_template('1618.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        new_user = User(name=name,email=email,password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')



    return render_template('register.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            session['email'] = user.email
            return redirect('/wikisearch')
        else:
            return render_template('login.html',error='Invalid user')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if session['email']:
        user = User.query.filter_by(email=session['email']).first()
        return render_template('dashboard.html',user=user)
    
    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('email',None)
    return redirect('/login')

@app.route('/romanian_empire')
def romanian_empire():
    return render_template('romanian_empire.html')

@app.route('/france')
def france():
    return render_template('france.html')

@app.route('/Roosevelt')
def Roosevelt():
    return render_template('Roosevelt.html')

@app.route('/Kenedy')
def Kenedy():
    return render_template('Kenedy.html')

@app.route('/OUN')
def OUN():
    return render_template('OUN.html')

@app.route('/sla')
def sla():
    return render_template('sla.html')

@app.route('/vilgelm')
def vilgelm():
    return render_template('vilgelm.html')

@app.route('/wikisearch')
def wikisearch():
    if session['email']:
        user = User.query.filter_by(email=session['email']).first()
    return render_template('wikisearch.html',user=user)

@app.route('/finlandia')
def finlandia():
    return render_template('finlandia.html')

@app.route('/che')
def che():
    return render_template('che.html')

@app.route('/mel')
def mel():
    return render_template('mel.html')

@app.route('/me1')
def me1():
    return render_template('me1.html')

@app.route('/wikiuser1')
def wikiuser1():
    audio_files = ['/static/roosevelt.mp3', '/static/kenedy.mp3', '/static/mus.mp3','/static/kastro.mp3','/static/goe.mp3','/static/chu.mp3','/static/ad.mp3']
    random_audio = random.choice(audio_files)
    if session['email']:
        user = User.query.filter_by(email=session['email']).first()
    return render_template('wikiuser1.html',user=user,random_audio=random_audio)

if __name__ == "__main__":
    app.run(debug=True)
