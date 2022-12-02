from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     PasswordField)
from wtforms.validators import InputRequired, Length

class RegisterForm(FlaskForm):
    email = StringField('email', validators =[InputRequired(), Length(max=50)])
    username = StringField('username', validators =[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators =[InputRequired(), Length(min=8, max=80)])