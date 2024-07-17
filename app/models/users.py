from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.sql import func
from app.database.db import Base

class User(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True, index=True)
  username = Column(Text(50), nullable=False, unique=True)
  password = Column(Text(100), nullable=False)
  role = Column(Text(20), nullable=False)
  created_at = Column(DateTime(timezone=True), server_default=func.now())