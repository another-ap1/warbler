from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import Optional, URL, NumberRange, AnyOf

class AddPetForm(FlaskForm):
    """Form for adding a new pet"""
    name = StringField("Pet Name")
    species = StringField("Species",
                          validators=[AnyOf(values=['Dog', 'Cat', 'Goblin'], message="species must be Dog, Cat, or Goblin")])
    photo_url = StringField("Photo URL",
                            validators=[Optional(), URL(require_tld=False, message="Please enter a valid URL")])
    age = IntegerField("Age", 
                       validators=[NumberRange(min=0, max=30, message="Age must be between 0-30")])
    notes = StringField("Notes")
    available = BooleanField("Available?")

class EditPetForm(FlaskForm):
    """Form for just the editing part"""
    photo_url = StringField("Photo URL",
                            validators=[Optional(), URL(require_tld=False, message="Please enter a valid URL")])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available?", validators=[Optional()])
