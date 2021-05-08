from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from flask import request
from werkzeug.urls import url_parse

@app.route('/')
def welcome():
    return render_template("welcome.html")

@app.route('/home')
def home():
    return render_template("Home.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password, please try again')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
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

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))