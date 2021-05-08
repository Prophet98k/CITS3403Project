from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email



class LoginForm(FlaskForm):
    email = StringField('*E-mail:', validators=[DataRequired(message='Please enter your email address'), Email(message='Please enter valid email address')])
    password = PasswordField('*Password:', validators=[DataRequired(message='Please enter your password')])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

