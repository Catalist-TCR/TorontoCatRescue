from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, TextAreaField, SelectField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired, Required
import json

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
	sex = SelectField('Sex', choices=[('m', 'M'),('f', 'F')])
	description = TextAreaField('Description')
	sn = SelectField('S/N', choices=[('y','Yes'),('n','No')])
	shelter_name = StringField('Shelter Name')
	shelter_id = StringField('Shelter ID')
	photo = FileField('Cat Photo')
	fiv_tested = SelectField('FIV Tested', choices=[('pos','Tested Positive'), ('neg', 'Tested Negative'), ('none','Not Tested')])
	flv_tested = SelectField('FLV Tested', choices=[('pos','Tested Positive'), ('neg', 'Tested Negative'), ('none','Not Tested')])
	fvrcp_vaccination_date = DateField('FVRCP Vaccination Date', format='%Y-%m-%d')
	rabies_vaccination_date = DateField('Rabies Vaccination Date', format='%Y-%m-%d')
	medical_notes = TextAreaField('Medical Notes')
	medical_documents = FileField('Medical Documents')
	behaviour_notes = TextAreaField('Behaviour Notes')
	urgent = BooleanField('Urgent')
	#INTAKE
	petpoint_id = StringField('Petpoint ID')
	outcome = TextAreaField('Outcome')
	intake_date = DateField('Intake Date', format='%Y-%m-%d')
	#FOSTER HOME
	foster_placement_date = DateField('Placement Date', format='%Y-%m-%d')
	location = StringField('Location')
	
	submit = SubmitField('Submit')
'''
	def __dict__(self): 
		def _try(o): 
			try: 
				return o.__dict__ 
			except: 
				return str(o)

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
'''

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