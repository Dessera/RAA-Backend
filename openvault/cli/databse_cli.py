from typer import Typer, Option
import asyncio
import json

from ..models import clear_db, init_db, generate_schema
from ..schemas.user_schema import UserCreateSchema
from ..services import user_service

subcommand = Typer()


@subcommand.command(help="创建所有数据库表")
def create():
    async def create_impl():
        try:
            await init_db()
            await generate_schema(True)
            print("全部数据库表已创建")
        except Exception as e:
            print(f"Error: {e}")

    asyncio.run(create_impl())


@subcommand.command(help="删除所有数据库表和数据")
def clear():
    async def clear_impl():
        try:
            await init_db()
            await clear_db()
            print("所有数据库表和数据已删除")
        except Exception as e:
            print(f"Error: {e}")

    asyncio.run(clear_impl())


@subcommand.command(help="加载用户数据到数据库")
def load_user(data_path: str = Option(help="加载用户数据的路径(json)")):
    async def load_user_impl(data_path: str):
        try:
            await init_db()
            with open(data_path, "r") as f:
                data_json = json.load(f)
            if not isinstance(data_json, list):
                print("数据格式应为列表")
                return
            success_count = 0
            for obj in data_json:
                schema = UserCreateSchema.model_validate(obj)
                await user_service.create_user(schema)
                success_count += 1
            print(f"{success_count} 条用户数据已加载")

        except Exception as e:
            print(f"加载数据时出错: {e}")

    asyncio.run(load_user_impl(data_path))


# @subcommand.command(help="加载数据到数据库")
# def load(
#     data_type: str = Option(help="加载数据的类型"),
#     data_path: str = Option(help="加载数据的路径(json)"),
# ):
#     async def load_data_impl(data_type: str, data_path: str):
#         await init_db()
#         models = get_db_models()
#         if data_type not in models.keys():
#             print(f"{data_type} 不可用")
#             print(f"可用的数据模型: {models.keys()}")
#             return
#         Model = models[data_type]
#         try:
#             with open(data_path, "r") as f:
#                 data_json = json.load(f)
#         except Exception as e:
#             print(f"Error reading data from {data_path}: {e}")
#             return
#         if not isinstance(data_json, list):
#             print("数据格式应为列表")
#             return
#         # create objects
#         model_objects = [Model(**data) for data in data_json]
#         for obj in model_objects:
#             await obj.save()
#         print(f"{len(model_objects)} 条数据已加载到 {data_type}")

#     asyncio.run(load_data_impl(data_type, data_path))
