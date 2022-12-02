from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy

#from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisthesecretkeyvalue011'
"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/c/Users/Dinah twirie/Desktop/theultimapp/database.db' 
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
"""

class LoginForm(FlaskForm):
    username = StringField('username', validators =[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators =[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')
    
class RegisterForm(FlaskForm):
    email = StringField('email', validators =[InputRequired(), Length(max=50)])
    username = StringField('username', validators =[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators =[InputRequired(), Length(min=8, max=80)])


@app.route('/')
def index():
    """
    form = LoginForm()
    if form.validate_on_submit():
        return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'"""
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    #to check if user already exists and if so redirect them to the dashboard
    if form.validate_on_submit():
        return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'
        """
        user= User.query.filter_by(username=form.username.data).first()
        if user:  
           # if user.password == form.password.data:
           if check_password_hash(user.password, form.password.data):
                return redirect(url_for('dashboard'))
        #if user doesn't exist...
        return '<h1>Invalid username or password</h1>'
        """
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    #to save data provided by the user to the sql database...... also instead of plaintext passwd, we can use the hashed one
    if form.validate_on_submit():
        return '<h1> + form.username.data + ' ' + form.password.data + </h1>'
    
        #new_user = User(username=form.username.data, email= form.email.data, password=form.password.data)
        """
         if user:  
             if user.password == form.password.data:
                 return redirect(url_for('dashboard'))
                
         db.session.add(new_user)
         db.session.commit()
         return '<h1>New user has been created!</h1>'
                #if user doesn't exist...
         #return '<h1>Invalid username or password</h1>'
         """
    return render_template('signup.html', form=form)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/serve')
def serve():
    return render_template('serve.html')


if __name__== '__main__':
    app.run(debug=True)
