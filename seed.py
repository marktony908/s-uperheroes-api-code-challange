from app import app, db
from models import Hero, Power, HeroPower

# Sample data
heroes_data = [
    {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
    {"name": "Doreen Green", "super_name": "Squirrel Girl"},
    {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
    {"name": "Janet Van Dyne", "super_name": "The Wasp"},
    {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
    {"name": "Carol Danvers", "super_name": "Captain Marvel"},
    {"name": "Jean Grey", "super_name": "Dark Phoenix"},
    {"name": "Ororo Munroe", "super_name": "Storm"},
    {"name": "Kitty Pryde", "super_name": "Shadowcat"},
    {"name": "Elektra Natchios", "super_name": "Elektra"}
]

powers_data = [
    {"name": "super strength", "description": "gives the wielder super-human strengths"},
    {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
    {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
    {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
]

hero_powers_data = [
    {"strength": "Strong", "hero_id": 1, "power_id": 1},
    {"strength": "Average", "hero_id": 1, "power_id": 2},
    {"strength": "Weak", "hero_id": 2, "power_id": 2},
    {"strength": "Strong", "hero_id": 3, "power_id": 3},
    {"strength": "Average", "hero_id": 4, "power_id": 4},
]

def seed_database():
    with app.app_context():
        # Drop existing data and create new tables
        db.drop_all()
        db.create_all()

        # Seed Heroes
        for hero_data in heroes_data:
            hero = Hero(**hero_data)
            db.session.add(hero)

        # Seed Powers
        for power_data in powers_data:
            power = Power(**power_data)
            db.session.add(power)

        # Commit the heroes and powers to the database
        db.session.commit()

        # Seed HeroPowers
        for hero_power_data in hero_powers_data:
            hero_power = HeroPower(**hero_power_data)
            db.session.add(hero_power)

        # Commit hero powers to the database
        db.session.commit()

if __name__ == '__main__':
    seed_database()
