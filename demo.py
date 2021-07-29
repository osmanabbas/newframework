from flask import Flask, render_template, url_for, flash, redirect
from flask_wtf import FlaskForm
#from wtforms import StringField, PasswordField, SubmitField, BooleanField
#from wtforms.validators import DataRequired, Length, Email, EqualTo
from forms import RegistrationForm
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = '749de9e5f51473163fcee00351f7bbb2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


db = SQLAlchemy(app)

db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(60), nullable=False)

  def __repr__(self):
    return f"User('{self.username}', '{self.email}')"



@app.route("/")
def hello_world():
    return "<p>Hello, SEO Tech Developers!</p>"



@app.route("/home")
def home():
    return render_template('home.html', subtitle='Home Page')
    
@app.route("/about")
def about():
    return render_template('about.html', subtitle='About Page')
  
@app.route("/register", methods=['GET','POST'])
def register():
    form=RegistrationForm()
    return render_template('register.html', subtitle='Register', form=form)



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")