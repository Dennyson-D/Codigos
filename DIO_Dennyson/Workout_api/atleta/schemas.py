from typing import Annotated, Optional
from pydantic import  Field, PositiveFloat
from categorias.schemas import CategoriaIn
from centro_treinamento.schemas import CentroTreinamentoAtleta
from contrib.schemas import BaseSchema, OutMixin


class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome atleta', exemple = 'Dennyson', max_length = 50)]
    cpf: Annotated[str, Field(description='CPF atleta', exemple = '12345678910' , max_length = 11)]
    idade: Annotated[int, Field(description='Idade atleta', exemple = 35)]
    peso: Annotated[PositiveFloat, Field(description='Peso atleta', exemple = 75)]
    altura: Annotated[PositiveFloat, Field(description='Altura atleta', exemple = 1.80)]
    sexo: Annotated[str, Field(description='Sexo atleta', exemple = 'M', max_length = 1)]
    categoria: Annotated[CategoriaIn, Field(description='Categoria do atleta')]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description='Centro de treinamento', exemple = 'M', max_length = 1)]


class AtletaIn(Atleta):
    pass

class AtletaOut(Atleta,OutMixin):
    pass    

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None,description='Nome atleta', exemple = 'Dennyson', max_length = 50)]
    idade: Annotated[Optional[int], Field(None,description='Idade atleta', exemple = 35)]   