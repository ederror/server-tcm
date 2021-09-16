from flask_sqlalchemy import SQLAlchemy
from flask import Flask

#db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///_static/trash.db'
db = SQLAlchemy(app)

class Trash(db.Model):
    tid = db.Column(db.Integer, primary_key=True)
    trash_name = db.Column(db.String(20), unique=True, nullable=False)
    trash_type = db.Column(db.String(20), unique=False, nullable=False)
    trash_howto_desc = db.Column(db.String(100), unique=False, nullable=False)
    trash_howto_id = db.Column(db.Integer, unique=False)

    def __repr__(self):
        return '<Trash %r, name %s>' % (self.tid, self.trash_name)
    
class Can(db.Model):
    cid = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(20), unique=True, nullable=False)
    trash_type = db.Column(db.String(20), unique=False, nullable=False)
    addr = db.Column(db.String(50), unique=False, nullable=False)
    detail_addr = db.Column(db.String(100), unique=False, nullable=True)
    latitude = db.Column(db.Float, unique=False, nullable=True)
    longitude = db.Column(db.Float, unique=False, nullable=True)