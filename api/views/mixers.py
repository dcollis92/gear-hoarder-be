from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.mixer import Mixer

mixers = Blueprint('mixers', 'mixers')

# Create Mic
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
