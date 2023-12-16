import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger, String, text
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(BigInteger)
    user_name: Mapped[str] = mapped_column(String(32), nullable=True)
    registration_at: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    status: Mapped[str] = mapped_column(String(12), server_default='Неактивен')
    partners: Mapped[int | None] = mapped_column(default=0)
    bots: Mapped[int | None] = mapped_column(default=0)
    account: Mapped[int] = mapped_column(default=0)
    completed: Mapped[int] = mapped_column(default=0)
    discarded: Mapped[int] = mapped_column(default=0)
