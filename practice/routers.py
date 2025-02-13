from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Body, Depends, Path, Query

from dependencies import serialize_task_model, IsSortedEnum, IsReversedEnum
from schemas import TaskCreateSchema, TaskResponseSchema

router = APIRouter(prefix='/v1', tags=['Router for TODO service'])


@router.post('/make-task')
async def make_task(
        task_schema: TaskResponseSchema = Depends(serialize_task_model),
) -> TaskResponseSchema:
    return task_schema


@router.get('/get/{task_id}')
async def get_task(
        task_id: Annotated[UUID, Path(...)],
) -> TaskResponseSchema:
    task = ...
    return task


@router.get('/tasks/{user_id}', response_model=list[TaskResponseSchema])
async def get_user_tasks(user_id: UUID = Path(...),
                         sorted: IsSortedEnum = Query(default=IsSortedEnum.No),
                         reversed: IsReversedEnum = Query(default=IsReversedEnum.No)
                         ) -> list[TaskResponseSchema]:
    pass

@router.patch('/update/{task_id}')
async def update_task(
        task_schema: TaskCreateSchema
) -> TaskResponseSchema:
    task: TaskResponseSchema = ...
    updated_data = task.update_data(task_schema)
    return updated_data
