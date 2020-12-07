from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
    
class CommentForm(FlaskForm):
    
    title = StringField('Comment title',validators=[Required()])

    comment = TextAreaField('Movie comment')

    submit = SubmitField('Submit')
 
class PitchForm(FlaskForm):
    title = StringField('Pitch Title')
    category = SelectField(u'Pitch Categories', choices=[('Inspirational', 'Inspirational'),('Work', 'Work'), ('Love', 'Love'),('Hustle', 'Hustle')])
    pitch = TextAreaField('Pitch')
    submit = SubmitField('Submit')
 
