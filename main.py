from flask import Flask, session, render_template, request, redirect, url_for, abort
from flask_dance.consumer import oauth_authorized
from flask_dance.contrib.google import make_google_blueprint, google
from werkzeug.utils import secure_filename
from form_classes import LoginForm, CatInformation
from google_sheets import find_permission, input_data, return_database
import os
from flask_wtf import CsrfProtect
import sys
import requests
import config

csrf = CsrfProtect()

GOOGLE_CLIENT_ID = config.OAUTH_CONFIG['GOOGLE_CLIENT_ID']
GOOGLE_CLIENT_SECRET = config.OAUTH_CONFIG['GOOGLE_CLIENT_SECRET']
STATIC_URL_PATH = '/static'
app = Flask(__name__, static_url_path=STATIC_URL_PATH)
app.config['SECRET_KEY'] = 'cats'

google_bp = make_google_blueprint(
	client_id=GOOGLE_CLIENT_ID,
	client_secret=GOOGLE_CLIENT_SECRET,
	scope=["https://www.googleapis.com/auth/plus.me",
		"https://www.googleapis.com/auth/userinfo.email"],
	authorized_url='/oauth2callback'
	)
app.register_blueprint(google_bp)

@oauth_authorized.connect_via(google_bp)
def logged_in(blueprint, token):
	respon_json = google.get('/oauth2/v2/userinfo').json()
	print(respon_json)
	session['access_token'] = token
	session['email'] = respon_json['email']

@app.route('/shelter_upload', methods=['GET', 'POST'])
def shelter_upload():
	if not google.authorized:
		return redirect(url_for("google.login"))


	form = CatInformation()
	if form.validate_on_submit():
		input_data(form, 'shelter')

		if form.photo.data is not None:
			pho = form.photo.data
			filename = secure_filename(pho.filename)
			pho.save(os.path.join(app.instance_path, 'photos', filename))

		if form.medical_documents.data is not None:
			med_docs = form.medical_documents.data
			filename = secure_filename(med_docs.filename)
			med_docs.save(os.path.join(app.instance_path, 'medical_documents', filename))
		
		return redirect(url_for('index'))
	else:
		print(form.errors)
		
	return render_template('shelter_upload.html', form=form, title="new")

@app.route('/intake_upload', methods=['GET', 'POST'])
def intake_upload():
	if not google.authorized:
		return redirect(url_for("google.login"))

	form = CatInformation()
	if form.validate_on_submit():
		input_data(form, 'intake')
		
		if form.photo.data is not None:
			pho = form.photo.data
			filename = secure_filename(pho.filename)
			pho.save(os.path.join(app.instance_path, 'photos', filename))

		if form.medical_documents.data is not None:
			med_docs = form.medical_documents.data
			filename = secure_filename(med_docs.filename)
			med_docs.save(os.path.join(app.instance_path, 'medical_documents', filename))
		
		return redirect(url_for('index'))
	else:
		print(form.errors)

	return render_template('intake_upload.html', form=form)

@app.route('/foster_upload', methods=['GET', 'POST'])
def foster_upload():
	if not google.authorized:
		return redirect(url_for("google.login"))
	

	form = CatInformation()
	if form.validate_on_submit():
		input_data(form, 'foster')
		
		if form.photo.data is not None:
			pho = form.photo.data
			filename = secure_filename(pho.filename)
			pho.save(os.path.join(app.instance_path, 'photos', filename))

		if form.medical_documents.data is not None:
			med_docs = form.medical_documents.data
			filename = secure_filename(med_docs.filename)
			med_docs.save(os.path.join(app.instance_path, 'medical_documents', filename))
		
		return redirect(url_for('index'))
	else:
		print(form.errors)
	return render_template('foster_upload.html', form=form, title="new")

@app.route('/database')
def database():
	if not google.authorized:
		return redirect(url_for("google.login"))
	
	card = return_database()
	card.pop(0)
	return render_template('database.html', cards=card, title="data")

@app.route('/waitlist')
def waitlist():
	if not google.authorized:
		return redirect(url_for("google.login"))
	
	card = return_database()
	card = [i for i in card if i[20]=="shelter"]
	return render_template('database.html', cards=card, title="wait")


@app.route('/')
def index():
	if not google.authorized:
		return redirect(url_for("google.login"))

	email = session.get('email')
	permission = find_permission(email)
	print(permission)
	print(email)

	if permission == 'shelter':
		return redirect(url_for('shelter_upload'))
	elif permission == 'intake':
		return redirect(url_for('intake_upload'))
	elif permission == 'foster':
		return redirect(url_for('foster_upload'))
	else:
		return("User not in system")

	# form = LoginForm()
	# return render_template('index.html', title='Sign In', form=form)

if __name__ == '__main__':
	os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
	app.jinja_env.auto_reload = True
	app.run(debug=True)


