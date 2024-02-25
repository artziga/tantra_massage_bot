__all__ = ("router", )

from aiogram import Router
from .base import router as base_commands_router
from .user_private import router as user_commands_router

router = Router(name=__name__)

router.include_router(base_commands_router)
router.include_router(user_commands_router)
