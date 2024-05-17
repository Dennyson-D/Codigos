from typing import Annotated
from pydantic import UUID4, Field
from contrib.schemas import BaseSchema


class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome CT', exemple = 'CT ABC', max_lenght=20)]
    endereco: Annotated[str, Field(description='Endereço CT', exemple = 'Rua abc ...', max_lenght=60)]
    proprietario: Annotated[str, Field(description='Proprietário CT', exemple = 'Dennyson', max_lenght=30)]

class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT King', max_length=20)]    

class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description='Identificador do centro de treinamento')]
