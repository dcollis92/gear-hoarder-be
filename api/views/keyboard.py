from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.keyboard import Keyboard

keyboards = Blueprint('keyboards', 'keyboards')

@keyboards.route('/', methods=["POST"])
@login_required
def create():
  data = request.get_json()
  profile = read_token(request)
  data["profile_id"] = profile["id"]

  keyboard = Keyboard(**data)
  db.session.add(keyboard)
  db.session.commit()
  return jsonify(keyboard.serialize()), 201


