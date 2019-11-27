import datetime
from . import db


class Client(db.Model):
    __tablename__ = "clients"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable= False)
    password = db.Column(db.String(300), nullable=False)
    client_name = db.Column(db.String(30), nullable=False)
    created_at = db.Column(db.DateTime)
    last_modified = db.Column(db.DateTime)

    def __init__(self, email, password, client_name):
        self.email = email
        self.password = password
        self.client_name = client_name
        self.created_at = datetime.datetime.now()
        self.last_modified = datetime.datetime.now()

    def save(self):
        db.session.add(self)
        db.session.commit()
        return 'Client successfully created'