from aiogram import Router

from .custom import setup_custom_routers
from .default import setup_default_router


def setup_all_routers():
    router = Router()
    router.include_router(setup_default_router())
    router.include_router(setup_custom_routers())
    return router
