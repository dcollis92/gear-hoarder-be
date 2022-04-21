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

# Index Interfaces
@interfaces.route('/', methods=["GET"])
def index():
  interfaces = Interface.query.all()
  return jsonify([interface.serialize() for interface in interfaces]), 201


@interfaces.route('/<id>', methods=["GET"])
def show(id):
  interface = Interface.query.filter_by(id=id).first()
  return jsonify(interface.serialize()), 200