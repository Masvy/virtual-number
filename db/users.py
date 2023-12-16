from sqlalchemy import select, update

from db.database import async_session
from db.model import Users


async def read_users(user_id):
    async with async_session() as session:
        result = await session.execute(select(Users).where(Users.user_id == user_id))
        user = result.all()
        return user


async def update_account(user_id, amount):
    async with async_session() as session:
        await session.execute(update(Users).where(Users.user_id == user_id).values(account=Users.account+amount))
        await session.execute(
            update(Users).where(Users.user_id == user_id).values(completed=Users.completed + amount))
        await session.commit()


async def subtract_money(user_id, amount):
    async with async_session() as session:
        await session.execute(update(Users).where(Users.user_id == user_id).values(account=Users.account-amount))
        await session.execute(
            update(Users).where(Users.user_id == user_id).values(discarded=Users.discarded + amount))
        if amount == 250:
            await session.execute(update(Users).where(Users.user_id == user_id).values(status='На месяц'))
        elif amount == 650:
            await session.execute(update(Users).where(Users.user_id == user_id).values(status='На 3 месяца'))
        else:
            await session.execute(update(Users).where(Users.user_id == user_id).values(status='На 6 месяцев'))
        await session.commit()


async def read_account(user_id):
    async with async_session() as session:
        result = await session.execute(select(Users.account).where(Users.user_id == user_id))
        account = result.scalar()
        return account


async def show_user_ids():
    async with async_session() as session:
        result = await session.execute(select(Users.user_id))
        user_ids = [row[0] for row in result]
        return user_ids
