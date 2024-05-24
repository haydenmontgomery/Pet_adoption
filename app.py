"""Blogly application."""
from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm

def create_app(database_name, testing=False):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql:///{database_name}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SECRET_KEY'] = "abc123"
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    if testing:
        app.config["WTF_CSRF_ENABLED"] = False

    debug = DebugToolbarExtension(app)
    app.app_context().push()
    connect_db(app)
    db.create_all()

    @app.route('/')
    def list_pets():
        """Lists all pets at the adoption center"""
        pets = Pet.query.all()
        return render_template('home.html', pets=pets)
    
    @app.route('/add', methods=["GET", "POST"])
    def add_pet():
        """Route for adding a pet for adoption"""
        form = PetForm()
        #species_list = ['Cat', 'Dog', 'Rabbit']
        #form.species.choices = species_list
        if form.validate_on_submit():
            name = form.name.data
            species = form.species.data
            photo_url = form.photo_url.data
            age = form.age.data
            notes = form.notes.data

            pet = Pet(name=name, species=species, photo_url=photo_url, age= age, notes=notes)
            db.session.add(pet)
            db.session.commit()
            return redirect('/')
        else:
            return render_template('add_pet_form.html', form=form)
        
    @app.route('/<int:id>', methods=["GET", "POST"])
    def edit_pet(id):
        """Route for editing a pet."""
        pet = Pet.query.get_or_404(id)
        form = PetForm(obj=pet)
        if form.validate_on_submit():
            pet.name = form.name.data
            pet.species = form.species.data
            pet.photo_url = form.photo_url.data
            pet.age = form.age.data
            pet.notes = form.notes.data
            db.session.commit()
            return redirect('/')
        else:
            return render_template("edit_pet_form.html", form=form)

    
    return app

if __name__=='__main__':
    app = create_app('pets')
    app.run(debug=True)