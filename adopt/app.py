from flask import Flask, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'donttellanyone'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']= False
debug = DebugToolbarExtension(app)

with app.app_context():
    connect_db(app)
    db.create_all()

@app.route('/')
def homepage():
    """Redirect to the homepage veiwing all pets"""

    return redirect('/pets')

@app.route('/pets')
def all_pets():
    """homepage that has all of the pets"""

    pets = Pet.query.all()

    return render_template('index.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """page for adding a new pet"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        age = form.age.data
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data

        new_pet = Pet(name=name, species=species, age=age, photo_url=photo_url, notes=notes, available=available)
        db.session.add(new_pet)
        db.session.commit()

        return redirect('/pets')
    
    else:
        return render_template('new_pet.html', form=form)
    
@app.route('/edit/<int:pet_id>', methods=["GET", "POST"])
def edit_pet(pet_id):
    """render the page to edit a pet and also handle post request"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.add(pet)
        db.session.commit()

        return redirect('/pets')
    
    else:
        return render_template('edit_pet.html', form=form, pet=pet)
    
@app.route('/delete/<int:pet_id>', methods=["POST"])
def delete_pet(pet_id):

    pet = Pet.query.get_or_404(pet_id)

    db.session.delete(pet)
    db.session.commit()

    return redirect('/pets')