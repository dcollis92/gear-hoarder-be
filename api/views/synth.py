from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.synth import Synth

synths = Blueprint('synths', 'synths')

@synths.route('/', methods=["POST"])
@login_required
def create():
  data = request.get_json()
  profile = read_token(request)
  data["profile_id"] = profile["id"]

  synth = Synth(**data)
  db.session.add(synth)
  db.session.commit()
  return jsonify(synth.serialize()), 201

@synths.route('/', methods=["GET"])
def index():
  synths = Synth.query.all()
  return jsonify([synth.serialize() for synth in synths]), 201

@synths.route('/<id>', methods=["GET"])
def show(id):
  synth = Synth.query.filter_by(id=id).first()
  return jsonify(synth.serialize()), 200

@synths.route('/<id>', methods=["PUT"])
def update(id):
  data = request.get_json()
  profile = read_token(request)
  synth = synth.query.filter_by(id=id).first()

  if synth.profile_id != profile["id"]:
    return 'Nah Bubba', 403

  for key in data:
    setattr(synth, key, data[synth])

  db.session.commit()
  return jsonify(synth.serialize()), 200