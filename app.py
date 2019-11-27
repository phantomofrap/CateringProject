from flask import Flask
import os
from models import db, ma
from services import bcrypt
from contollers import auth_blueprint,event_blueprint, jwt

app = Flask(__name__)




app.config.from_object('config.Development')


db.init_app(app)
ma.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(event_blueprint, url_prefix="/event")




if __name__ == '__main__':
    app.run()