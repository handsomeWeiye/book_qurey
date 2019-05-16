from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class Updata (FlaskForm):
    author = StringField('author',validators=[DataRequired()])
    book = StringField('book',validators=[DataRequired()])
    submit = SubmitField()