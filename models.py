from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Trash(db.Model):
    tid = db.Column(db.Integer, primary_key=True)
    trash_name = db.Column(db.String(20), unique=True, nullable=False)
    trash_type = db.Column(db.String(20), unique=False, nullable=False)
    trash_howto_desc = db.Column(db.String(100), unique=False, nullable=False)
    trash_howto_id = db.Column(db.Integer, unique=False)

    def __repr__(self):
        return '<Trash %r>' % self.tid