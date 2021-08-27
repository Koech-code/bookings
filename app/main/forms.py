from datetime import date
from flask_wtf import FlaskForm
from wtforms import DateField,SelectField,SubmitField,StringField
from flask_datepicker import datepicker
from wtforms.fields.html5 import DateField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import ValidationError, Required

class BookForm(FlaskForm):
    service=SelectField('Select Service',choices=[('',''),("Salon","Salon"),("Barbershop","Barbershop")],validators=[Required()])
    tarehe=DateField('Date')
    email=StringField('Email') 
    submit=SubmitField('Book')
    

class FeedbackForm(FlaskForm):
    
    name=StringField('Full name')
    email=StringField('Email') 
    message=TextAreaField('Message')
    submit=SubmitField('Leave a feedbck')