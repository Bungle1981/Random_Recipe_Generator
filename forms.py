from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    Ingredients=StringField(validators=[DataRequired()])
    submit=SubmitField("Get my random recipe...")
