from datetime import datetime
from typing import Annotated
from pydantic import UUID4, BaseModel, Field
from sqlalchemy import DateTime


class BaseSchema(BaseModel):
    class config:
        extra = 'forbid'
        from_attributes = True

class OutMixin(BaseSchema):  
    id: Annotated [UUID4, Field(description='Identificador')]
    created_at: Annotated[datetime, Field('Data de criação')]