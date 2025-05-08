class Plan(db.Model):
    __tablename__ = 'plan'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    plan_name = db.Column(db.String(50), nullable=False)
    plan_price = db.Column(db.Float, nullable=False)
    expiration_date = db.Column(db.String(50), nullable=False)
    plan_duration = db.Column(db.String(50), nullable=False)
    purchase_date = db.Column(db.String(50), nullable=False)
    purchase_time = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "plan_name": self.plan_name,
            "plan_price": self.plan_price,
            "expiration_date": self.expiration_date,
            "plan_duration": self.plan_duration,
            "purchase_date": self.purchase_date,
            "purchase_time": self.purchase_time
        }
