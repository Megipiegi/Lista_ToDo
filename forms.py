from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.core import BooleanField
from wtforms.validators import DataRequired

    
class TodoForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    done = BooleanField('done', validators=[DataRequired()])