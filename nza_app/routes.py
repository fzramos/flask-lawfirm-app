from nza_app import app, db
from flask import render_template,request,url_for,redirect
from nza_app.forms import UserInfoForm, LoginForm
from nza_app.models import User, Note, check_password_hash
from flask_login import login_required,login_user, current_user, logout_user


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        # Saving the logged in user to a variable
        logged_user = User.query.filter(User.email == email).first()
        # check the password of the newly found user
        # and validate the password against the hash value
        # inside of the database
        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html', login_form = form)

@app.route('/register', methods = ['GET','POST'])
def register():
    form = UserInfoForm()
    # Validation of our form
    if request.method == 'POST' and form.validate():
        # Get Information from the form
        username = form.username.data
        email = form.email.data
        password = form.password.data
        # print the data to the server that comes from the form
        print(username,email,password)

        # Creation/Init of our User Class (aka Model)
        user = User(username,email,password)
        
        #Open a connection to the database
        db.session.add(user)  

        # Commit all data to the database
        db.session.commit()

        return redirect(url_for('login'))
        
    return render_template('register.html',user_form = form)

