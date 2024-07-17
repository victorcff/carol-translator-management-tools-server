from sqlalchemy import Column, Integer, DateTime, ForeignKey, Text
from sqlalchemy.sql import func
from app.database.db import Base

class Event(Base):
  __tablename__ = "events"
  id = Column(Integer, primary_key=True, index=True)
  name = Column(Text(50), nullable=False)
  contractor_id = Column(Integer, ForeignKey("users.id"))
  interpreter_id = Column(Integer, ForeignKey("users.id"))
  date = Column(DateTime(timezone=True), server_default=func.now())
  payment_id = Column(Integer, ForeignKey("payments.id"))
  created_at = Column(DateTime(timezone=True), server_default=func.now())