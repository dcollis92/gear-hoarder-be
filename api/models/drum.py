from datetime import datetime
from api.models.db import db


class Drum(db.Model):
    __tablename__ = 'drums'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100))
    make = db.Column(db.String(100))
    model = db.Column(db.String(100))
    color = db.Column(db.String(100))
    year = db.Column(db.String(4))
    description = db.Column(db.String(250))
    bass_drum_size = db.Column(db.String(10))
    tom_amount = db.Column(db.String(5))
    floor_tom_size = db.Column(db.String(10))
    total_pieces = db.Column(db.String(5))
    is_working = db.Column(db.Boolean, default=True, nullable=False)
    on_loan = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))
    
    def __repr__(self):
      return f"Drum('{self.id}', '{self.make}', '{self.model}', '{self.type}'"
      
    def serialize(self):
      drum = {g.name: getattr(self, g.name) for g in self.__table__.columns}
      return drum