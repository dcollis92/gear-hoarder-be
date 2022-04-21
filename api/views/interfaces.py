from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.interface import Interface

interfaces = Blueprint('interfaces', 'interfaces')

# Create Interface
@interfaces.route('/', methods=["POST"])
@login_required
def create():
  data = request.get_json()
  profile = read_token(request)
  data["profile_id"] = profile["id"]

  interface = Interface(**data)
  db.session.add(interface)
  db.session.commit()
  return jsonify(interface.serialize()), 201