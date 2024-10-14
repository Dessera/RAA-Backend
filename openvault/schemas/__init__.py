from tortoise import Tortoise
from ..models import SCHEMAS

Tortoise.init_models(SCHEMAS, "models")
