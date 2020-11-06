from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired,EqualTo, Email

class NoteForm(FlaskForm): 
    case_name = StringField('Title', validators = [DataRequired()])
    case_note = TextAreaField('Content', validators = [DataRequired()])
    submit = SubmitField()