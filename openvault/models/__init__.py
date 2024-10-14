from tortoise import Tortoise
from tortoise.contrib.fastapi import RegisterTortoise
from functools import partial
from ..config import CONFIG

SCHEMAS = [
    f"{__name__}.user_model",
    f"{__name__}.group_model",
]

# FastAPI lifespan 使用的初始化数据库函数
register_orm = partial(
    RegisterTortoise,
    db_url=CONFIG.database_url,
    modules={"models": SCHEMAS},
)


async def init_db():
    """初始化数据库连接，在 FastAPI 外部使用。"""
    await Tortoise.init(
        db_url=CONFIG.database_url,
        modules={"models": SCHEMAS},
    )


async def clear_db():
    """
    清除所有的数据库表和数据，在 FastAPI 外部使用
    WARNING: 这个函数会清除所有的数据表和数据，且依赖了 Tortoise 的内部实现，不要在生产环境使用。
    """
    conn = Tortoise.get_connection("default")
    Models = Tortoise.apps["models"]
    # temporary disable foreign key check
    await conn.execute_script("SET FOREIGN_KEY_CHECKS=0;")
    for Model in Models.values():
        # drop table
        await conn.execute_script(
            f"DROP TABLE IF EXISTS {Model._meta.db_table} CASCADE;"
        )
        print(f"Table {Model._meta.db_table} dropped.")


def get_db_models():
    return Tortoise.apps["models"]


async def generate_schema(safe: bool = False):
    """生成数据库表结构，在 FastAPI 外部使用"""
    await Tortoise.generate_schemas(safe)
