from flask_wtf import FlaskForm
from wtforms import (BooleanField, DateField, DateTimeField, EmailField, IntegerField, PasswordField, RadioField, SelectField, SelectMultipleField, StringField, SubmitField, TextAreaField)
from wtforms.validators import DataRequired, Email, Length, NumberRange, InputRequired, ValidationError

class RegisterForm(FlaskForm):
    """Form to register a new user"""
    
    username = StringField('Username', render_kw={'placeholder': 'Username'}, validators=[DataRequired()])
    password = PasswordField('Password', render_kw={'placeholder': 'Password'}, validators=[DataRequired()])
    email = EmailField('Email Address', render_kw={'placeholder': 'Are you on e-mail?'}, validators=[Email()])
    zipcode = StringField('ZIP Code', render_kw={'placeholder': 'ZIP Code'}, validators=[Length(min=5, 
                                                                                                max=5, 
                                                                                                message='Only 5-digit U.S. ZIP codes accepted')])
    submit = SubmitField('Create Profile')
    
class LoginForm(FlaskForm):
    """Form to log a user in"""
    
    username = StringField('Username', render_kw={'placeholder': 'Enter your username'}, validators=[DataRequired()])
    password = PasswordField('Password', render_kw={'placeholder': 'Enter your password'}, validators=[DataRequired()])
    submit = SubmitField('Submit')
    
