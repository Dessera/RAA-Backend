from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from .config import CONFIG
from .models import register_orm

from .routers import include_app_routers
from .error import include_app_error_handlers


@asynccontextmanager
async def general_lifespan(app: FastAPI):
    async with register_orm(app):
        yield


def create_app(lifespan=general_lifespan) -> FastAPI:
    """创建FastAPI实例，挂载路由、中间件、错误处理等

    Returns:
        FastAPI: FastAPI实例
    """
    app = FastAPI(title="EJob-DB", lifespan=lifespan)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[CONFIG.app_base_url],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    include_app_routers(app)
    include_app_error_handlers(app)

    return app


app = create_app()
