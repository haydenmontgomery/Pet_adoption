from models import db, connect_db, Pet
from app import create_app

# Create all tables
app = create_app("pets", testing=False)
#connect_db(app)
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

mabel = Pet(name="Mabel", species="Cat", photo_url="https://images.unsplash.com/photo-1582725461742-8ecd962c260d?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", age=3, notes="Cute cat!")
nina = Pet(name="Nina", species="Cat", photo_url="https://images.unsplash.com/photo-1518791841217-8f162f1e1131?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fHRhYmJ5JTIwY2F0fGVufDB8fDB8fHww", age=5)
theo = Pet(name="Theo", species="Dog", photo_url="https://images.unsplash.com/photo-1647107303671-71a8e02e7aa0?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8cmF0JTIwdGVycmllcnxlbnwwfHwwfHx8MA%3D%3D", age=3, notes="Great with kids!")
malcolm = Pet(name="Malcolm", species="TDog", age=7, notes="Perfect dog ready for a good home!")
ruby = Pet(name="Ruby", species="Rabbit", photo_url="https://images.unsplash.com/photo-1706533078696-95f8db1c6947?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fGxpb25oZWFkJTIwYnVubnl8ZW58MHx8MHx8fDA%3D", age=2, notes="Lionhead rabbit who is great with other pets")
mochi = Pet(name="Mochi", species="Rabbit", age=1)

db.session.add_all([mabel,nina,theo,malcolm,ruby,mochi])
db.session.commit()