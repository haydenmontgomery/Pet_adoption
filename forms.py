from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, URLField
from wtforms.validators import InputRequired, NumberRange

class PetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired(message="Pet name cannot be blank")])
    species = SelectField("Species", choices=['Cat', 'Dog', 'Rabbit'])
    photo_url = URLField("Photo URL")
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30, message="Age should be between 0 and 30")])
    notes = StringField("Notes")