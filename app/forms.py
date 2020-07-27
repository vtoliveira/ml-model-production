from flask_wtf import FlaskForm

from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired


class ModelInputForm(FlaskForm):
    id = StringField('id', validators=[DataRequired()])
    score_3 = FloatField('score_3', validators=[DataRequired()])
    score_4 = FloatField('score_4', validators=[DataRequired()])
    score_5 = FloatField('score_5', validators=[DataRequired()])
    score_6 = FloatField('score_6', validators=[DataRequired()])
    income = FloatField('income', validators=[DataRequired()])
    submit = SubmitField('Send Input')