from nza_app import app, db
from flask import render_template,request,url_for,redirect
from nza_app.forms import UserInfoForm, LoginForm, NoteForm
from nza_app.models import User, Note, check_password_hash
from flask_login import login_required,login_user, current_user, logout_user

@app.route('/notes/create', methods = ['GET', 'POST'])
@login_required
def posts():
    form = NoteForm()

    if request.method == 'POST' and form.validate():
        case_name = form.case_name.data
        case_note = form.case_note.data
        user_id = current_user.id
        note = Note(case_name, case_note ,user_id)

        db.session.add(note)

        db.session.commit()
        return redirect(url_for('show_notes'))
    return render_template('newnote.html', form = form)

# Create new note
#     newnote.html

# shows all notes for user
#     notes.html

@app.route('/notes')
@login_required
def show_notes():
    # test this!!
    notes = Note.query.filter(Note.user_id == current_user.id).all()

    return render_template('notes.html', user_notes = notes)

@app.route('/notes/<int:note_id>')
@login_required
def note_detail(note_id):
    note = Note.query.get_or_404(note_id)
    return render_template('note_detail.html', note = note)

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
            return redirect(url_for('show_notes'))
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


# Update Note Route -- 
@app.route('/notes/update/<int:note_id>', methods = ['GET', 'POST'])
@login_required
def note_update(note_id): 
    note = Note.query.get_or_404(note_id)
    form = NoteForm()
    if request.method == 'POST' and form.validate():
        case_name = form.case_name.data
        case_note = form.case_note.data
        user_id = current_user.id
        # Update the Database with the new Info 
        note.case_name = case_name
        note.case_note = case_note

        # Commit the changes to the database
        db.session.commit()
        return redirect(url_for('show_notes'))
    return render_template('note_update.html', update_form = form)

# Delete Route 
@app.route('/notes/delete/<int:note_id>', methods = ['GET', 'DELETE'])
@login_required
def note_delete(note_id): 
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('show_notes'))
