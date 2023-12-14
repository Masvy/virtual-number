from sqlalchemy import select

from db.database import async_session
from db.model import Users


async def read_users(user_id):
    async with async_session() as session:
        result = await session.execute(select(Users).where(Users.user_id == user_id))
        user = result.all()
        return user
