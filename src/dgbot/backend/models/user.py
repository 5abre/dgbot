from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship
from dgbot.backend.models.base import Base

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
