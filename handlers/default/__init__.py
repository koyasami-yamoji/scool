from aiogram import Router

from . import start, formula


def setup_default_router():
    router = Router()
    router.include_router(start.router)
    router.include_router(formula.router)
    return router
