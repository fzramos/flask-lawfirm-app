from nza_app import app, db
from flask import render_template,request, redirect, url_for
# from nza_app.forms import UserInfoForm, LoginForm
from nza_app.models import User, Note, check_password_hash
from flask_login import login_required,login_user, current_user, logout_user

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/what_we_do')
def what_we_do():
    return render_template('what.html')