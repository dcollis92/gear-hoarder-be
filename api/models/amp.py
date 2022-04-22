from datetime import datetime
from api.models.db import db

class Amp(db.Model):
    __tablename__ = 'amps'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100))
    make = db.Column(db.String(100))
    model = db.Column(db.String(100))
    wattage = db.Column(db.Integer)
    speaker_size = db.Column(db.String(5))
    speaker_amount = db.Column(db.String(5))
    power_type = db.Column(db.String(100))
    ohm_rating = db.Column(db.String(100))
    finish = db.Column(db.String(100))
    year = db.Column(db.String(4))
    description = db.Column(db.String(250))
    condition = db.Column(db.String(510))
    is_modified = db.Column(db.Boolean, default=False, nullable=False)
    mod_description = db.Column(db.String(250))
    broken = db.Column(db.Boolean, default=False, nullable=False)
    on_loan = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))
    
    def __repr__(self):
      return f"Amp('{self.id}', '{self.make}', '{self.model}', '{self.type}'"
      
    def serialize(self):
      amp = {a.name: getattr(self, a.name) for a in self.__table__.columns}
      return amp