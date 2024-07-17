from sqlalchemy import Column, Integer, DateTime, ForeignKey, Float, Boolean
from sqlalchemy.sql import func
from app.database.db import Base

class Payment(Base):
  __tablename__ = "payments"
  id = Column(Integer, primary_key=True, index=True)
  value = Column(Float, nullable=False)
  estimated_date = Column(DateTime(timezone=True), server_default=func.now())
  done = Column(Boolean, nullable=False)