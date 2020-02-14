# Electron Wizard webapp
# 
# @file  : forms.py
# @brief : Provides I/O operation via forms
# @author: Rutuparn Pawar (InputBlackBoxOutput)
# @date_created : 9 Feb, 2020
#

try:
	from flask_wtf import FlaskForm
	from wtforms import DecimalField, RadioField, SelectField
	from wtforms.validators import DataRequired, Optional, InputRequired
except ImportError:
	print('Error occured while importing modules')

# Ohms law
class Ohm(FlaskForm):
    R = DecimalField('R', validators=[Optional()])
    V = DecimalField('V', validators=[Optional()])
    I = DecimalField('I', validators=[Optional()])

# Resistors in series/parallel
class R_Comb(FlaskForm):
    Rone = DecimalField('R1', validators=[DataRequired()])
    Rtwo = DecimalField('R2', validators=[DataRequired()])

# Through hole resistor value
band_list =[('black','black'), ('brown','brown')]
class R(FlaskForm):
	
	n_bands = RadioField('Number of bands on resistor', validators=[DataRequired], choices=[('3','3'),('4','4'),('5','5')])
	colour1 = SelectField('Band 1', validators=[DataRequired()], choices=band_list )
	colour2 = SelectField('Band 2', validators=[DataRequired()], choices=band_list )
	colour3 = SelectField('Band 3', validators=[DataRequired()], choices=band_list )
	colour4 = SelectField('Band 4', validators=[Optional()], choices=band_list)
	colour5 = SelectField('Band 5', validators=[Optional()], choices=band_list)

# SMD Resistor value
# SMD Capacitor value
# SMD Inductor value
class SMD(FlaskForm):
	compnt = RadioField('Select component', validators=[DataRequired], choices=['Resistor','Capacitor','Inductor'])
	code = DecimalField('Code', validators=[DataRequired()])

# Voltage divider
class V_Div(FlaskForm):
	V = DecimalField('V', validators=[DataRequired()])
	R1 = DecimalField('R1', validators=[DataRequired()])
	R2 = DecimalField('R2', validators=[DataRequired()])



# LED resistor
class LED_R(FlaskForm):
	Vdrop = DecimalField('Vdrop', validators=[DataRequired()])
	V = DecimalField('V', validators=[DataRequired()])
	I = DecimalField('I', validators=[DataRequired()])



