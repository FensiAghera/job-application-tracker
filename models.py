from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum, Date, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
import enum

class StatusEnum(str, enum.Enum):
    Applied = "Applied"
    Interview = "Interview"
    Rejected = "Rejected"
    Offer = "Offer"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    applications = relationship("Application", back_populates="owner", cascade="all, delete")

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    status = Column(Enum(StatusEnum), default=StatusEnum.Applied)
    location = Column(String, nullable=True)
    salary_min = Column(Integer, nullable=True)
    salary_max = Column(Integer, nullable=True)
    applied_date = Column(Date, nullable=True)
    notes = Column(Text, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    owner = relationship("User", back_populates="applications")