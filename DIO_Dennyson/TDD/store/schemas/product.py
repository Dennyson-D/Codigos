
from datetime import datetime
from typing import Annotated, Optional
import uuid
from bson import Decimal128
from pydantic import UUID4, AfterValidator, BaseModel, Field, Decimal, model_validator
from store.schemas.base import BaseSchemaMixin, OutMixin

class ProductBase(BaseModel):
    name: str = Field(...,description="Product name") # ..., significa que é campo obrigatório
    quantity: int = Field(...,description="Product quantity")
    price: Decimal = Field(...,description="Product price")
    status: bool =  Field(...,description ="Product status")

class ProductIn(ProductBase,BaseSchemaMixin):
    ...   

class ProductOut(ProductIn, OutMixin):
    ...
    
def convert_decimal_128(v):   
    return Decimal128() 

Decimal_ = Annotated[Decimal,AfterValidator(convert_decimal_128)]    

class ProductUpdate(BaseSchemaMixin):
    quantity: Optional[int] = Field(None,description="Product quantity")
    price: Optional[Decimal] = Field(None,description="Product price")
    status: Optional[bool] =  Field(None,description ="Product status")

class ProductUpdateOut(ProductOut):
    ...
