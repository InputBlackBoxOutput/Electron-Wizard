from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class R(FlaskForm):
    r = StringField('R1', validators=[DataRequired()])
    submit = SubmitField('Submit')

