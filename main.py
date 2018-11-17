from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


@app.route('/')
def main():
	form = LoginForm()
	return render_template('index.html', title='Sign In', form=form)

def application():
	STATIC_URL_PATH = '/static/'
	app = Flask(__name__, static_url_path=STATIC_URL_PATH)
	app.config['SECRET_KEY'] = 'cats'
	app.run(debug=True)