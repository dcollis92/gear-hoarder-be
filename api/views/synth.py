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

