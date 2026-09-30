from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime

from database import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    card_id = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String(20), default="PENDING")
    created_at = Column(DateTime, default=datetime.utcnow)