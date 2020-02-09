from flask_wtf import FlaskForm 
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

# Form for serial and parallel resistance calculation
class SrlPrllRes():
	r1 = StringField('R1')
	r2 = StringField('R2') #validators=[]

	calculate = SubmitField('Calculate')