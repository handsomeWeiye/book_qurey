from qurey_systerm import db
from datetime import datetime

class Data (db.Model):
    id = db.Column(db.INTEGER,primary_key=True)
    author = db.Column(db.String)
    book = db.Column(db.String)
    timestamp = db.Column(db.DateTime,default=datetime.utcnow())