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