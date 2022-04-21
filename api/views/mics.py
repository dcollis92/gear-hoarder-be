from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.mic import Mic

mics = Blueprint('mics', 'mics')

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

@mics.route('/', methods=["GET"])
def index():
  mics = Mic.query.all()
  return jsonify([mic.serialize() for mic in mics]), 201

@mics.route('/<id>', methods=["GET"])
def show(id):
  mic = Mic.query.filter_by(id=id).first()
  return jsonify(mic.serialize()), 200
