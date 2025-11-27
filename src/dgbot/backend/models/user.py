from sqlalchemy import BigInteger, String, Date, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from dgbot.backend.models.base import Base
from datetime import date, datetime

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    phone_number: Mapped[str] = mapped_column(String(20), nullable=True)
    last_activity: Mapped[date] = mapped_column(Date)
    consecutive_days: Mapped[int] = mapped_column(Integer, default=0)