from flask_wtf import FlaskForm
from wtforms import DecimalField, RadioField, SelectField
from wtforms.validators import DataRequired

# 1) Ohms law
class Ohm(FlaskForm):
    R = DecimalField('R', default=-1)
    V = DecimalField('V', default=-1)
    I = DecimalField('I', default=-1)

# 2) Through hole resistor value
class R(FlaskForm):
	n_bands = RadioField('Number of bands on resistor', validators=[DataRequired], choices=['3','4','5'])
	color1 = SelectField('Band 1', validators=[DataRequired()])
	color2 = SelectField('Band 2', validators=[DataRequired()])
	color3 = SelectField('Band 3', validators=[DataRequired()])
	color4 = SelectField('Band 4', default=None)
	color5 = SelectField('Band 5', default=None)

# 3) SMD Resistor value
# 4) SMD Capacitor value
# 5) SMD Inductor value
class SMD(FlaskForm):
	compnt = RadioField('Select component', validators=[DataRequired], choices=['Resistor','Capacitor','Inductor'])
	code = DecimalField('Code', validators=[DataRequired()])

# 6) Voltage divider
class V_Div(FlaskForm):
	V = DecimalField('V', validators=[DataRequired()])
	R1 = DecimalField('R1', validators=[DataRequired()])
	R2 = DecimalField('R2', validators=[DataRequired()])

# 7) Resistors in series/parallel
class R_Comb(FlaskForm):
    Rone = DecimalField('R1', validators=[DataRequired()])
    Rtwo = DecimalField('R2', validators=[DataRequired()])

# 8) LED resistor
class LED_R(FlaskForm):
	Vdrop = DecimalField('Vdrop', validators=[DataRequired()])
	V = DecimalField('V', validators=[DataRequired()])
	I = DecimalField('I', validators=[DataRequired()])



