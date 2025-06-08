from aiogram import Router

from .users import router as user_router



router = Router()

router.include_routers(user_router)