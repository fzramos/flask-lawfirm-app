from nza_app import app, db
from flask import render_template, request, url_for, redirect
from nza_app.forms import NoteForm
from nza_app.models import User, Note, check_password_hash
from flask_login import login_required,login_user, current_user, logout_user

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