from enum import Enum
from typing import Annotated

from fastapi import Body

from schemas import TaskResponseSchema, TaskCreateSchema


def serialize_task_model(
        create_task_schema: Annotated[TaskCreateSchema, Body(...)]
) -> TaskResponseSchema:
    task_response_schema = TaskResponseSchema(**create_task_schema.dict())
    return task_response_schema


class IsSortedEnum(Enum):
    Yes = True
    No = False
class IsReversedEnum(Enum):
    Yes = True
    No = False
