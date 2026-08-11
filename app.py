from flask import Flask,render_template,request,redirect,session
from api import sentiment_analysis, summarize_txt,abuse_detn
from dotenv import load_dotenv
import os

from db import Database

app = Flask(__name__)
dbo=Database()
app.secret_key=os.getenv("SECRET_KEY")


@app.route('/')
def index():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/perform_registration' ,methods=['post'])
def perform_registration():
    name=request.form.get('user_name')
    email=request.form.get('user_email')
    password=request.form.get('user_password')


    response=dbo.insert(name,email,password)

    if response:
        return render_template('login.html',message1 = 'Email registered kindly login')
    else:
        return render_template('register.html',message='Email already exist')

@app.route('/perform_login',methods=['post'])
def perform_login():
    email = request.form.get('user_email')
    password = request.form.get('user_password')

    response=dbo.search(email,password)

    if response:
        session['logged_in']=1
        return redirect('/profile')
    else:
        return render_template('login.html',message='Incorrect email/password')

@app.route('/profile')
def profile():
    if session.get('logged_in'):
        return render_template('profile.html')
    else:
        return redirect('/')
@app.route('/summary')
def summary():
    if session.get('logged_in'):
        return render_template('summary.html')
    else:
        return redirect('/')
@app.route('/perform_summary',methods=['GET','POST'])
def perform_summary():
    if session.get('logged_in'):
        if request.method=='POST':
            text=request.form.get('summarize_text')
            summary=summarize_txt(text)

            return render_template('summary.html',summary=summary)
        return render_template('summary.html')
    else:
        return redirect('/')

@app.route('/abuse_det')
def abuse_det():
    if session.get('logged_in'):
        return render_template('abuse_det.html')
    else:
        return redirect('/')

@app.route('/perform_abuse_det',methods=['GET','POST'])
def perform_abuse_det():
    if session.get('logged_in'):
        if request.method=='POST':
            text=request.form.get('abuse_det')
            det=abuse_detn(text)

            return render_template('abuse_det.html',abuse_det=det)
        return render_template('abuse_det.html')
    else:
        return redirect('/')

@app.route('/sentiment_analysis')
def senti_analysis():
    if session.get('logged_in'):
        return render_template('senti.html')
    else:
        return redirect('/')
@app.route('/perform_sentiment_analysis',methods=['GET','POST'])
def perform_senti_analysis():
    if session.get('logged_in'):
        if request.method=='POST':
            text=request.form.get('sentiment_analysis')
            det=sentiment_analysis(text)

            return render_template('senti.html',sentiment_analysis=det)
        return render_template('senti.html')
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
