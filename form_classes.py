from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired




class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class CatInformation(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    documents = FileField(validators=[FileRequired()])



'''

Proposal Date
Name
Age
Sex
Description
S/N
Shelter Name
Shelter ID
Petpoint ID (Unique Identifier)
Image
FIV Tested (+/-) - Tested Positive, Tested Negative, Not Tested (default)
FLV Tested (+/-) - Tested Positive, Tested Negative, Not Tested (default)
FVRCP Vaccination Date
Rabies Vaccination Date
Medcial Notes
Behaviour Notes
Outcome - Entered into TCR program, euthanized, etc.
Intake Date
Foster Placement Date
Location - Dropdown

'''