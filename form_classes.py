from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, TextAreaField, SelectField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired, Required




class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')

class CatInformation(FlaskForm):
	date = DateField('Date', format='%Y-%m-%d')
	name = StringField('Cat Name', validators=[DataRequired()])
	date_of_birth = DateField('Date of Birth', format='%Y-%m-%d')
	age = StringField('Age')
	sex = SelectField('Sex', choices=['M','F'], validators=[Required()])
	description = TextAreaField('Description')
	sn = SelectField('S/N', choices=['Yes','No'], validators=[Required()])
	shelter_name = StringField('Shelter Name', validators=[DataRequired()])
	shelter_id = StringField('Shelter ID', validators=[DataRequired()])
	photo = FileField('Cat Photo', validators=[FileRequired()])
	fiv_tested = SelectField('FIV Tested', choices=['Tested Positive', 'Tested Negative', 'Not Tested'], validators=[Required()])
	flv_tested = SelectField('FLV Tested', choices=['Tested Positive', 'Tested Negative', 'Not Tested'], validators=[Required()])
	fvrcp_vaccination_date = DateField('FVRCP Vaccination Date', format='%Y-%m-%d')
	rabies_vaccination_date = DateField('Rabies Vaccination Date', format='%Y-%m-%d')
	medical_notes = TextAreaField('Medical Notes')
	medical_documents = FileField('Medical Documents', validators=[FileRequired()])
	behaviour_notes = TextAreaField('Behaviour Notes')
	#INTAKE
	petpoint_id = StringField('Petpoint ID', validators=[DataRequired()])
	outcome = TextAreaField('Entered into TCR program, euthanized, etc.')
	intake_date = DateField('Intake Date', format='%Y-%m-%d')
	#FOSTER HOME
	foster_placement_date = DateField('Placement Date', format='%Y-%m-%d')
	location = SelectField('Location', choices=['Tested Positive', 'Tested Negative', 'Not Tested'], validators=[Required()])
	
	submit = SubmitField('Submit')


'''

xProposal Date
xName
XDoB
xAge
xSex
xDescription
xS/N
xShelter Name
xShelter ID
-----Petpoint ID (Unique Identifier)
xImage
xFIV Tested (+/-) - Tested Positive, Tested Negative, Not Tested (default)
xFLV Tested (+/-) - Tested Positive, Tested Negative, Not Tested (default)
xFVRCP Vaccination Date
xRabies Vaccination Date
xMedcial Notes
xMedical Forms
xBehaviour Notes
-----Outcome - Entered into TCR program, euthanized, etc.
-----Intake Date
-----Foster Placement Date
-----Location - Dropdown

'''