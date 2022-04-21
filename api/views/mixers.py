from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.mixer import Mixer

mixers = Blueprint('mixers', 'mixers')

# Create Mixer
@mixers.route('/', methods=["POST"])
@login_required
def create():
  data = request.get_json()
  profile = read_token(request)
  data["profile_id"] = profile["id"]

  mixer = Mixer(**data)
  db.session.add(mixer)
  db.session.commit()
  return jsonify(mixer.serialize()), 201

# Index Mixers
@mixers.route('/', methods=["GET"])
def index():
  mixers = Mixer.query.all()
  return jsonify([mixer.serialize() for mixer in mixers]), 201

# Show Mixer
@mixers.route('/<id>', methods=["GET"])
def show(id):
  mixer = Mixer.query.filter_by(id=id).first()
  return jsonify(mixer.serialize()), 200

# Update Mixer
@mixers.route('/<id>', methods=["PUT"])
def update(id):
  data = request.get_json()
  profile = read_token(request)
  mixer = Mixer.query.filter_by(id=id).first()

  if mixer.profile_id != profile["id"]:
    return 'Nah Bubba', 403

  for key in data:
    setattr(mixer, key, data[mixer])

  db.session.commit()
  return jsonify(mixer.serialize()), 200

# Delete Mixer
@mixers.route('/<id>', methods=["DELETE"])
def delete(id):
  profile = read_token(request)
  mixer = Mixer.query.filter_by(id=id).first()

  if mixer.profile_id != profile["id"]:
    return 'Nah Bubba', 403

  db.session.delete(mixer)
  db.session.commit()
  return jsonify(message="Success"), 200

@mixers.errorhandler(Exception)          
def basic_error(err):
  return jsonify(err=str(err)), 500