# Electron Wizard webapp
# 
# @file  : forms.py
# @brief : Provides I/O operation via forms
# @author: Rutuparn Pawar (InputBlackBoxOutput)
# @date_created : 9 Feb, 2020
#

try:
	from flask_wtf import FlaskForm
	from wtforms import IntegerField, DecimalField, RadioField, SelectField, BooleanField, StringField
	from wtforms.validators import DataRequired, Optional
except ImportError:
	print('Error occured while importing modules required by forms.py')

# ////////////////////////////////////////////////////////////////////////////////////////////////////
# SI unit prefixes
prefix = ['p', 'n', 'u', 'm', '', 'k', 'M', 'G']
vList = [(x+'V', x+'V') for x in prefix]
iList = [(x+'A', x+'A') for x in prefix]
rList = [(x+'ohm', x+'ohm') for x in prefix]


class Unit(FlaskForm):
	unitV1 = SelectField('', validators=[DataRequired()], choices=vList, default='V')
	unitV2 = SelectField('', validators=[DataRequired()], choices=vList, default='V')

	unitI1 = SelectField('', validators=[DataRequired()], choices=iList, default='A')
	unitI2 = SelectField('', validators=[DataRequired()], choices=iList, default='A')
	
	unitR1 = SelectField('', validators=[DataRequired()], choices=rList, default='ohm')
	unitR2 = SelectField('', validators=[DataRequired()], choices=rList, default='ohm')
	unitRl = SelectField('', validators=[DataRequired()], choices=rList, default='ohm')
	
# ////////////////////////////////////////////////////////////////////////////////////////////////////

# Ohms law
class Ohm(Unit):

	R = DecimalField('R', validators=[Optional()])
	V = DecimalField('V', validators=[Optional()])
	I = DecimalField('I', validators=[Optional()])


# Resistors in series/parallel
class R_Comb(Unit):
	sp = RadioField('In', choices=[('S','Series'),('P','Parallel')], default='S')
	Rone = DecimalField('R1', validators=[DataRequired()])
	Rtwo = DecimalField('R2', validators=[DataRequired()])


# Through hole resistor value
clrSet =['None','Black','Brown','Red','Orange','Yellow','Green','Blue','Violet','Grey','White','Gold','Silver']
bandList = [(x,x) for x in clrSet]

class R(Unit):
	
	nbands = RadioField('Number of bands on resistor', choices=[('3','3'),('4','4'),('5','5')], default ='3')
	colour1 = SelectField('Band 1', validators=[DataRequired()], choices=bandList )
	colour2 = SelectField('Band 2', validators=[DataRequired()], choices=bandList )
	colour3 = SelectField('Band 3', validators=[DataRequired()], choices=bandList )
	colour4 = SelectField('Band 4', validators=[Optional()], choices=bandList)
	colour5 = SelectField('Band 5', validators=[Optional()], choices=bandList)

# SMD Resistor value
# SMD Capacitor value
# SMD Inductor value
class SMD(Unit):
	compnt = RadioField('Select component:', choices=[('R','Resistor'),('C','Capacitor'),('I','Inductor')], default='R')
	code = StringField('Code', validators=[DataRequired()])
	underlined = BooleanField('Underlined ?')

# Voltage divider
class V_Div(Unit):
	Vin = DecimalField('Vi', validators=[Optional()])	
	Vout = DecimalField('Vo', validators=[Optional()])
	Rload = DecimalField('Rl', validators=[Optional()])
	R1 = DecimalField('R1', validators=[Optional()])
	R2 = DecimalField('R2', validators=[Optional()])

LEDclrSet =['Ignore colour','Red','Yellow','Orange','Blue','Green','Violet','UV','White']
LEDclrlist = [(x,x) for x in LEDclrSet]


# LED resistor
class LED_R(Unit):
	LEDclr = SelectField('LED Colour:', validators=[DataRequired()], choices=LEDclrlist, default='Ignore colour')	
	Vsrc = DecimalField('Vsrc', validators=[DataRequired()])	
	Ilim = DecimalField('Ilim', validators=[DataRequired()])


# LED resistor
class RPwr(Unit):
	R = DecimalField('R', validators=[DataRequired()])
	V = DecimalField('V', validators=[Optional()])
	I = DecimalField('I', validators=[Optional()])

clrSetL0 =['None','Black','Brown','Red','Orange','Yellow','Green','Blue','Violet','Grey','White']
bandListL0 = [(x,x) for x in clrSetL0]

clrSetL1 =['None','Black','Brown','Red','Orange','Yellow','Gold','Silver']
bandListL1 = [(x,x) for x in clrSetL1]

# Inductor colour code
class I(Unit):
	colour1 = SelectField('Band 1', validators=[DataRequired()], choices=bandListL0)
	colour2 = SelectField('Band 2', validators=[DataRequired()], choices=bandListL0)
	colour3 = SelectField('Band 3', validators=[DataRequired()], choices=bandListL1)
	colour4 = SelectField('Band 4', validators=[Optional()], choices=bandListL1)

# Reactance
# Improvise by adding resonance condition
class React(Unit):
	compnt = RadioField('Component:', validators=[DataRequired()], choices=[('C','Capacitor'), ('I','Inductor')], default='C')
	val = DecimalField('Value', validators=[DataRequired()])
	freq = DecimalField('Freq', validators=[DataRequired()])





