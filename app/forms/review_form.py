from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import ValidationError, DataRequired

class ReviewForm(FlaskForm):
    
    content = StringField('Review', [DataRequired()])