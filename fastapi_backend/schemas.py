from pydantic import BaseModel


class PaymentCreate(BaseModel):
    user_id: int
    card_id: int
    amount: float