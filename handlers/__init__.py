from .information import information_router
from .profile import profile_router
from .start import start_router

routers_list = [
    start_router,
    information_router,
    profile_router,
]

__all__ = [
    'routers_list',
]
