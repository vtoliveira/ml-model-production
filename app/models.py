from datetime import datetime

from app import db


class RequestModel(db.Model):
    __tablename__ = 'requests'

    id = db.Column(db.String(120), primary_key=True)
    score_3 = db.Column(db.Float)
    score_4 = db.Column(db.Float)
    score_5 = db.Column(db.Float)
    score_6 = db.Column(db.Float)
    income = db.Column(db.Float)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    