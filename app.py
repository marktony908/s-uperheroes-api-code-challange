from flask import Flask, jsonify, request
from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()  # Create database tables

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes])

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if hero:
        return jsonify(hero.to_dict())
    return jsonify({'error': 'Hero not found'}), 404

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers])

@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if power:
        return jsonify(power.to_dict())
    return jsonify({'error': 'Power not found'}), 404

@app.route('/powers', methods=['POST'])
def create_power():
    data = request.json
    try:
        new_power = Power(
            name=data['name'],
            description=data['description']
        )
        db.session.add(new_power)
        db.session.commit()
        return jsonify(new_power.to_dict()), 201
    except Exception as e:
        db.session.rollback()  # Roll back any changes if there's an error
        return jsonify({'error': str(e)}), 500




if __name__ == '__main__':
    app.run(debug=True)
