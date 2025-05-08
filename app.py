import os
from flask import Flask, request, jsonify
from models import db, Plan

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://auth_db_24g7_user:aYSW6NK6OimiOnOBKqOI470dc2oGNeQ3@dpg-d08tlp1r0fns73dpsn90-a.oregon-postgres.render.com/auth_db_24g7_ehtf'



app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def create_tables():
    with app.app_context():
        db.create_all()

@app.route('/purchase-plan', methods=['POST'])
def purchase_plan():
    data = request.get_json()

    required_fields = ["email", "plan_name", "plan_price", "expiration_date", "plan_duration", "purchase_date", "purchase_time"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing fields in request"}), 400

    plan = Plan(
        email=data['email'],
        plan_name=data['plan_name'],
        plan_price=float(data['plan_price']),
        expiration_date=data['expiration_date'],
        plan_duration=data['plan_duration'],
        purchase_date=data['purchase_date'],
        purchase_time=data['purchase_time']
    )

    db.session.add(plan)
    db.session.commit()

    return jsonify({"message": "Plan purchased successfully"}), 201


@app.route('/transaction-history', methods=['POST'])
def transaction_history():
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({"error": "Email is required"}), 400

    plans = Plan.query.filter_by(email=email).all()

    if not plans:
        return jsonify({"error": "No transactions found for this email"}), 404

    history = []
    total_purchase = 0.0

    for plan in plans:
        history.append({
            "plan_name": plan.plan_name,
            "plan_price": plan.plan_price,
            "expiration_date": plan.expiration_date,
            "plan_duration": plan.plan_duration,
            "purchase_date": plan.purchase_date,
            "purchase_time": plan.purchase_time
        })
        total_purchase += plan.plan_price

    response = {
        "email": email,
        "transaction_history": history,
        "total_purchase": round(total_purchase, 2)
    }

    return jsonify(response), 200


if __name__ == '__main__':
    with app.app_context():
        create_tables()
    app.run(debug=True)
