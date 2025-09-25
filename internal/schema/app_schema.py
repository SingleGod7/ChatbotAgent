from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class CompletionReq(FlaskForm):
    query = StringField('query', validators=[
        DataRequired(message="Query is required."),
        Length(min=1, max=1000, message="Query must be between 1 and 1000 characters.")
    ])