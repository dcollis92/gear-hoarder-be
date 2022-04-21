from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.mic import Mic

mics = Blueprint('mics', 'mics')

# Create Mic
@mics.route('/', methods=["POST"])
@login_required
def create():
  data = request.get_json()
  profile = read_token(request)
  data["profile_id"] = profile["id"]

  mic = Mic(**data)
  db.session.add(mic)
  db.session.commit()
  return jsonify(mic.serialize()), 201

# Index Mics
@mics.route('/', methods=["GET"])
def index():
  mics = Mic.query.all()
  return jsonify([mic.serialize() for mic in mics]), 201

# Show Mic
@mics.route('/<id>', methods=["GET"])
def show(id):
  mic = Mic.query.filter_by(id=id).first()
  return jsonify(mic.serialize()), 200

# Update Mic
@mics.route('/<id>', methods=["PUT"])
def update(id):
  data = request.get_json()
  profile = read_token(request)
  mic = Mic.query.filter_by(id=id).first()

  if mic.profile_id != profile["id"]:
    return 'Nah Bubba', 403

  for key in data:
    setattr(mic, key, data[mic])

  db.session.commit()
  return jsonify(mic.serialize()), 200

# Delete Mic
@mics.route('/<id>', methods=["DELETE"])
def delete(id):
  profile = read_token(request)
  mic = Mic.query.filter_by(id=id).first()

  if mic.profile_id != profile["id"]:
    return 'Nah Bubba', 403

  db.session.delete(mic)
  db.session.commit()
  return jsonify(message="Success"), 200

@mics.errorhandler(Exception)          
def basic_error(err):
  return jsonify(err=str(err)), 500
