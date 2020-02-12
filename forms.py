from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# 1) Ohms law
class Ohm(FlaskForm):
    R = StringField('R', validators=[])
    V = StringField('V', validators=[])
    I = StringField('I', validators=[])

# 2) Through hole resistor value
class R(FlaskForm):
	color1 = StringField('Band 1', validators=[DataRequired()])

# 3) SMD Resistor value
# 4) SMD Capacitor value
# 5) SMD Inductor value
class SMD(FlaskForm):
	M = StringField('Marking', validators=[DataRequired()])

# 6) Voltage divider
class V_Div(FlaskForm):
	V = StringField('V', validators=[DataRequired()])
	R1 = StringField('R1', validators=[DataRequired()])
	R2 = StringField('R2', validators=[DataRequired()])

# 7) Resistors in series/parallel
class R_Comb(FlaskForm):
    Rone = StringField('R1', validators=[DataRequired()])
    Rtwo = StringField('R2', validators=[DataRequired()])

# 8) LED resistor
class LED_R(FlaskForm):
	Vdrop = StringField('Vdrop', validators=[DataRequired()])
	V = StringField('V', validators=[DataRequired()])
	I = StringField('I', validators=[DataRequired()])



