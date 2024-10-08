from flask import request, jsonify
from app import app, db
from models import Hero, Power, HeroPower

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes])

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    return jsonify(hero.to_dict())

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers])

@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify(power.to_dict())

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    description = request.json.get('description')
    if description and len(description) >= 20:
        power.description = description
        db.session.commit()
        return jsonify(power.to_dict())
    return jsonify({"errors": ["Validation errors"]}), 400

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    hero_id = request.json.get('hero_id')
    power_id = request.json.get('power_id')
    strength = request.json.get('strength')
    hero_power = HeroPower(hero_id=hero_id, power_id=power_id, strength=strength)
    db.session.add(hero_power)
    db.session.commit()
    return jsonify(hero_power.to_dict()), 201
