from fastapi import FastAPI
from fastapi.responses import JSONResponse
from tortoise.exceptions import DoesNotExist, MultipleObjectsReturned, IntegrityError


def include_app_error_handlers(app: FastAPI):
    """注册应用程序错误处理程序

    Args:
        app (FastAPI): FastAPI 实例
    """
    # database error handler
    app.add_exception_handler(DoesNotExist, __handle_not_found_error)
    app.add_exception_handler(MultipleObjectsReturned, __handle_multiple_objects_error)
    app.add_exception_handler(IntegrityError, __handle_integrity_error)

    # unknown error handler
    app.add_exception_handler(Exception, __handle_unknown_error)


def __handle_not_found_error(_, exc):
    return JSONResponse(
        status_code=404,
        content={"message": "服务器找不到请求的资源", "detail": str(exc)},
    )


def __handle_multiple_objects_error(_, exc):
    return JSONResponse(
        status_code=400,
        content={"message": "服务器找到多个匹配的资源", "detail": str(exc)},
    )


def __handle_integrity_error(_, exc):
    return JSONResponse(
        status_code=400,
        content={"message": "数据库约束错误", "detail": str(exc)},
    )


def __handle_unknown_error(_, exc):
    return JSONResponse(
        status_code=500,
        content={"message": "未知错误", "detail": str(exc)},
    )
