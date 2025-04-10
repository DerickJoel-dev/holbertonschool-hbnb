#!/usr/bin/env python3

from hbnb.app import create_app, db
from hbnb.app.models.user import User
from hbnb.app.models.place import Place
from hbnb.app.models.amenity import Amenity
from hbnb.app.models.review import Review

app = create_app()

with app.app_context():
    print("🔄 Resetting database...")
    db.drop_all()
    db.create_all()

    print("👤 Creating users...")
    user1 = User(first_name="Alice", last_name="Smith", email="alice@example.com", password="123456")
    user1.set_password("123456")
    user2 = User(first_name="Bob", last_name="Johnson", email="bob@example.com", password="password")
    user2.set_password("password")

    db.session.add_all([user1, user2])
    db.session.commit()

    print("🏡 Creating places...")
    place1 = Place(
        name="Beautiful Beach House",
        description="Enjoy the ocean breeze and stunning sunsets.",
        price=200.0,
        latitude=18.4655,
        longitude=-66.1057,
        owner_id=user1.id
    )
    place2 = Place(
        name="Cozy Cabin",
        description="A peaceful retreat surrounded by nature.",
        price=120.0,
        latitude=18.47,
        longitude=-66.11,
        owner_id=user1.id
    )
    place3 = Place(
        name="Modern Apartment",
        description="Perfect for city explorers with modern comfort.",
        price=150.0,
        latitude=18.48,
        longitude=-66.09,
        owner_id=user2.id
    )

    db.session.add_all([place1, place2, place3])
    db.session.commit()

    print("🛋 Creating amenities...")
    wifi = Amenity(name="WiFi")
    pool = Amenity(name="Pool")
    ac = Amenity(name="Air Conditioning")

    db.session.add_all([wifi, pool, ac])
    db.session.commit()

    print("🔗 Linking amenities to places...")
    place1.amenities.extend([wifi, pool, ac])
    place2.amenities.extend([wifi, ac])
    place3.amenities.extend([wifi])
    db.session.commit()

    print("⭐ Creating reviews...")
    review1 = Review(text="Amazing stay with great view!", rating=5, user_id=user2.id, place_id=place1.id)
    review2 = Review(text="Very cozy and clean. Loved it!", rating=4, user_id=user1.id, place_id=place2.id)

    db.session.add_all([review1, review2])
    db.session.commit()

    print("✅ Done seeding database.")
