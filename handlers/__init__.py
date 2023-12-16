from .information import information_router
from .profile import profile_router
from .admin import admin_router
from .start import start_router

routers_list = [
    admin_router,
    start_router,
    information_router,
    profile_router,
]

__all__ = [
    'routers_list',
]
