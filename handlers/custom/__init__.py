from aiogram import Router

from . import equations, get_count_equations, next_equation


def setup_custom_routers():
    router = Router()
    router.include_router(equations.router)
    router.include_router(get_count_equations.router)
    router.include_router(next_equation.router)
    return router
