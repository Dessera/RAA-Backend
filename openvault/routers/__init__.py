from fastapi import FastAPI
from . import user_router, group_router


def include_app_routers(app: FastAPI):
    """挂载路由

    Args:
        app (FastAPI): FastAPI实例
    """
    app.include_router(user_router.router)
    app.include_router(group_router.router)
