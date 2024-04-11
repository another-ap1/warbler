from models import Pet, db
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()
    Pet.query.delete()

"""Adding some default pets"""
dog1 = Pet(name='Thomas', 
           species='Mut', 
           photo_url="https://cdn.pixabay.com/photo/2024/02/05/16/23/labrador-8554882_1280.jpg", 
           age=12, 
           notes="Dearly missed")
dog2 = Pet(name='Penny', 
           species='Border Collie', 
           photo_url="https://cdn.pixabay.com/photo/2024/02/26/19/39/monochrome-image-8598798_1280.jpg", 
           age=8, 
           notes="So cute")
dog3 = Pet(name='Ernie', 
           species='Blue Heeler', 
           photo_url="https://cdn.pixabay.com/photo/2023/04/28/14/37/dog-7956839_1280.jpg", 
           age=1, 
           notes="Hes a heeler...")
cat1 = Pet(name='Coach Steve', 
           species='white', 
           age=10, 
           notes="Its a cat")
cat2 = Pet(name='The pilgrim', 
           species='black', 
           age=2)
cat3 = Pet(name='Magic Johnson', 
           species='multi', 
           age=1, 
           notes="Dude, please just take him", 
           available=False)

with app.app_context():
    db.session.add_all([dog1, dog2, dog3, cat1, cat2, cat3])
    db.session.commit()
