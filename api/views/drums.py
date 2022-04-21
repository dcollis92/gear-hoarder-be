from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.drum import Drum

drums = Blueprint('drums', 'drums')

@drums.route('/', methods=["POST"])
@login_required
def create():
  data = request.get_json()
  profile = read_token(request)
  data["profile_id"] = profile["id"]

  drum = Drum(**data)
  db.session.add(drum)
  db.session.commit()
  return jsonify(drum.serialize()), 201

@drums.route('/', methods=["GET"])
def index():
  drums = Drum.query.all()
  return jsonify([drum.serialize() for drum in drums]), 201

@drums.route('/<id>', methods=["GET"])
def show(id):
  drum = Drum.query.filter_by(id=id).first()
  return jsonify(drum.serialize()), 200

@drums.route('/<id>', methods=["PUT"])
@login_required
def update(id):
  data = request.get_json()
  profile = read_token(request)
  drum = Drum.query.filter_by(id=id).first()

  if drum.profile_id != profile["id"]:
    return 'Nah Bubba', 403
  
  for key in data:
    setattr(drum, key, data[key])
  
  db.session.commit()
  return jsonify(drum.serialize()), 200

@drums.route('<id>', methods=["DELETE"])
@login_required
def delete(id):
  profile = read_token(request)
  drum = Drum.query.filter_by(id=id).first()

  if drum.profile_id != profile["id"]:
    return 'Nah Bubba', 403

  db.session.delete(drum)
  db.session.commit()
  return jsonify(message="Success"), 200

