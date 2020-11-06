from nza_app import app, db
from flask import render_template,request, url_for, redirect
from nza_app.forms import UserForm, LoginForm, NoteForm
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
    notes = Note.query.filter(user_id == current_user.id).all()

    return render_template('notes.html', user_notes = notes)

@app.route('/notes/<int:note_id>')
@login_required
def note_detail(note_id):
    note = Note.query.get_or_404(note_id)
    return render_template('note_detail.html', note = note)