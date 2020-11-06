from nza_app import app, db
from flask import render_template,request
from nza_app.forms import UserInfoForm, LoginForm
from nza_app.models import User, Note, check_password_hash
from flask_login import login_required,login_user, current_user, logout_user
