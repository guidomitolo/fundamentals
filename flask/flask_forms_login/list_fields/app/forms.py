from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
# required for form list
from wtforms import Form, FormField, FieldList

from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class ProductForm(Form):
    title = StringField('Title')
    price = IntegerField('Price')

class InventoryForm(FlaskForm):
    category_name = StringField('Category Name')
    # the name of the list (which includes the fields)
    products = FieldList(FormField(ProductForm), min_entries=4, max_entries=8)