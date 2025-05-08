# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Plan(db.Model):
    __tablename__ = 'plan'  # optional, sets custom table name

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    plan_name = db.Column(db.String(100), nullable=False)
    plan_price = db.Column(db.Float, nullable=False)
    expiration_date = db.Column(db.String(20), nullable=False)
    plan_duration = db.Column(db.String(50), nullable=False)
    purchase_date = db.Column(db.String(20), nullable=False)
    purchase_time = db.Column(db.String(20), nullable=False)
