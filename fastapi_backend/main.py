import random

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, Base, get_db
from models import Payment
from schemas import PaymentCreate

app = FastAPI(
    title="Credit Card Payment API",
    description="Payment processing API for the Credit Card Payment System",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {
        "message": "Credit Card Payment API is running"
    }

@app.post("/payments/")
def create_payment(
    payment: PaymentCreate,
    db: Session = Depends(get_db)
):
    new_payment = Payment(
        user_id=payment.user_id,
        card_id=payment.card_id,
        amount=payment.amount,
        status="PENDING"
    )

    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)

    return {
        "message": "Payment created successfully",
        "payment_id": new_payment.id,
        "user_id": new_payment.user_id,
        "card_id": new_payment.card_id,
        "amount": new_payment.amount,
        "status": new_payment.status
    }

@app.put("/payments/{payment_id}/process")
def process_payment(
    payment_id: int,
    db: Session = Depends(get_db)
):
    payment = db.query(Payment).filter(Payment.id == payment_id).first()

    if not payment:
        return {
            "message": "Payment not found"
        }
        
    if payment.status != "PENDING":
        return {
            "message": "Payment has already been processed",
            "payment_id": payment.id,
            "status": payment.status
        }

    payment.status = random.choice(["SUCCESS", "FAILED"])

    db.commit()
    db.refresh(payment)

    return {
        "message": "Payment processed successfully",
        "payment_id": payment.id,
        "status": payment.status
    }

@app.get("/payments/{payment_id}")
def get_payment(
    payment_id: int,
    db: Session = Depends(get_db)
):
    payment = db.query(Payment).filter(Payment.id == payment_id).first()

    if not payment:
        return {
            "message": "Payment not found"
        }

    return {
        "payment_id": payment.id,
        "user_id": payment.user_id,
        "card_id": payment.card_id,
        "amount": payment.amount,
        "status": payment.status
    }

@app.get("/payments/")
def get_all_payments(
    db: Session = Depends(get_db)
):
    payments = db.query(Payment).all()

    return [
        {
            "payment_id": payment.id,
            "user_id": payment.user_id,
            "card_id": payment.card_id,
            "amount": payment.amount,
            "status": payment.status
        }
        for payment in payments
    ]