from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField, FloatField, SelectField, DateField, IntegerField
from wtforms.validators import DataRequired

rivers = ['MF Feather', "SF American", "Cherry Creek(Upper Tuolumne)"]
water_level_choices = ['Too High','Rictor','High','Medium High', 'medium Low', 'Low', 'Bones low', 'Too low']

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[ DataRequired ()])
    submit = SubmitField('Submit')

class RiverForm(FlaskForm):
    riverSection = SelectField('Section of River', choices=rivers, validators=[DataRequired()])
    difficulty = FloatField('Perceived Difficulty', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    flow = IntegerField('Flow', validators=[DataRequired()])
    water_level = SelectField('Water Level', choices=water_level_choices, validators=[DataRequired()])
    submit = SubmitField('Submit')
