from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from form_classes import LoginForm, CatInformation
import os






def application():
	STATIC_URL_PATH = '/static/'
	app = Flask(__name__, static_url_path=STATIC_URL_PATH)
	app.config['SECRET_KEY'] = 'cats'

	@app.route('/upload', methods=['GET', 'POST'])
	def upload():
		form = CatInformation()
		if form.validate_on_submit():
			print("It worked!!")
			f = form.documents.data
			filename = secure_filename(f.filename)
			f.save(os.path.join(
			    app.instance_path, 'photos', filename
			))
			return redirect(url_for('index'))
		return render_template('upload.html', form=form)

	@app.route('/')
	def index():
		form = LoginForm()
		return render_template('index.html', title='Sign In', form=form)

	app.run(debug=True)


application()