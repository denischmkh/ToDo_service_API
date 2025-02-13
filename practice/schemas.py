import datetime
from typing import Self

from pydantic import BaseModel, Field, model_validator, model_serializer
from uuid import uuid4, UUID


class TaskCreateSchema(BaseModel):
    user_id: UUID
    title: str = Field(max_length=50)
    description: str = Field(max_length=255)



class TaskResponseSchema(TaskCreateSchema):
    id: UUID = Field(default_factory=uuid4)
    completed: bool = False
    created: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)

    def update_data(self, updated_data: TaskCreateSchema) -> Self:
        self_data = self.dict()
        self_data.update(**updated_data.dict())
        self.__init__(**self_data)
        return self






