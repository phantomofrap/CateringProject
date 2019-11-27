from datetime import datetime
from . import db
from marshmallow import Schema, fields

class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    menu_choice = db.Column(db.Integer, nullable=False)
    event_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime)
    last_modified = db.Column(db.DateTime)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)

    def __init__(self, title, menu_choice, event_date, created_at, last_modified, client_id):
        self.title = title
        self.menu_choice = menu_choice
        self.event_date = event_date
        self.created_at = created_at
        self.last_modified = last_modified
        self.client_id = client_id

    def save(self):
        db.session.add(self)
        db.session.commit()
        return 'Event successfully created'

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return 'Event successfully deleted'
        
    def update(self, old, data):
        for k, v in data.items():
            setattr(old, k, v)
        self.last_modified = datetime.utcnow()
        db.session.commit()
        return old 

    @staticmethod
    def get_one_event(event_id):
        return Event.query.filter_by(id=event_id).first()

    @staticmethod
    def get_all_events():
        return Event.query.all()

class EventSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    menu_choice = fields.Int(required=True)
    event_date = fields.Str(required=True)
    client_id = fields.Int(required=True)