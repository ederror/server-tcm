from flask_sqlalchemy import SQLAlchemy
from flask import Flask

#db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///C:/Users/Shim/Desktop/Git/server-for-tfm/_static/trash.db'
db = SQLAlchemy(app)

class Trash(db.Model):
    tid = db.Column(db.Integer, primary_key=True)
    trash_name = db.Column(db.String(20), unique=True, nullable=False)
    trash_type = db.Column(db.String(20), unique=False, nullable=False)
    trash_howto_desc = db.Column(db.String(100), unique=False, nullable=False)
    trash_howto_id = db.Column(db.Integer, unique=False)

    def __repr__(self):
        return '<Trash %r, name %s>' % (self.tid, self.trash_name)