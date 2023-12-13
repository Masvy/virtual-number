from typing import Any, Awaitable, Callable, Dict, Union

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

from db.model import Users
from db.database import async_session


class RegisterCheck(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Union[Message, CallbackQuery],
            data: Dict[str, Any]):
        session_maker: sessionmaker = async_session
        async with session_maker() as session:
            async with session.begin():
                result = await session.execute(select(Users).where(Users.user_id == event.from_user.id))
                user = result.scalar()

                if user is not None:
                    pass
                else:
                    user = Users(
                        user_id=event.from_user.id,
                        user_name=event.from_user.username
                    )
                    await session.merge(user)

        return await handler(event, data)
