from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm


@app.route('/')
def welcome():
    return render_template("welcome.html")

@app.route('/home')
def home():
    return render_template("Home.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        flash('Login requested for user {}, remember_me={}'.format(
            form.email.data, form.remember_me.data))
        return redirect('/home')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/learn')
def learn():
    return render_template("learn.html")

@app.route('/accessment_home')
def accessment_home():
    return render_template("accessment_home.html")

@app.route('/accessment')
def accessment():
    return render_template("accessment.html")


@app.route('/table')
def table():
    return render_template("table.html")
