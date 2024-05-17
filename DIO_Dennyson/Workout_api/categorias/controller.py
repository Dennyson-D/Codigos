from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status, Query
from pydantic import BaseModel, UUID4
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from categorias.models import CategoriaModel
from categorias.schemas import CategoriaIn, CategoriaOut
from contrib.dependencies import DatabaseDependency

router = APIRouter()

class AtletaOut(BaseModel):
    nome: str
    centro_treinamento: str
    categoria: str

@router.post(
        '/', 
        summary='Criar nova categoria',
        status_code=status.HTTP_201_CREATED, 
        response_model=CategoriaOut,                      
)                
async def post(db_session: DatabaseDependency, categoria_in: CategoriaIn = Body(...)) -> CategoriaOut:
    categoria_out = CategoriaOut(id=uuid4(), **categoria_in.model_dump())
    categoria_model = CategoriaModel(**categoria_out.model_dump())
    db_session.add(categoria_model)
    await db_session.commit()
    return categoria_out

@router.get(
        '/', 
        summary='Consultar categorias',
        status_code=status.HTTP_200_OK, 
        response_model=list[CategoriaOut], 
)                
async def query(db_session: DatabaseDependency) -> list[CategoriaOut]:
    categorias: list[CategoriaOut] = (await db_session.execute(select(CategoriaModel))).scalars().all()
    return categorias

@router.get(
        '/{id}', 
        summary='Consultar uma categoria por id',
        status_code=status.HTTP_200_OK, 
        response_model=CategoriaOut, 
)                
async def query(id: UUID4, db_session: DatabaseDependency) -> CategoriaOut:
    categoria: CategoriaOut = (await db_session.execute(select(CategoriaModel).filter_by(id=id))).scalars().first()
    if not categoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Categoria não encontrada no id:{id}')
    return categoria

# Novos endpoints para Atleta
@router.get(
        '/atleta/', 
        summary='Consultar atletas',
        status_code=status.HTTP_200_OK,
        response_model=list[AtletaOut],
)
async def query_atleta(db_session: DatabaseDependency, nome: str = Query(None), cpf: str = Query(None)) -> list[AtletaOut]:
    query = select(CategoriaModel)
    
    if nome:
        query = query.filter(CategoriaModel.nome == nome)
    if cpf:
        query = query.filter(CategoriaModel.cpf == cpf)
        
    atletas: list[CategoriaModel] = (await db_session.execute(query)).scalars().all()
    atletas_out = [AtletaOut(nome=atleta.nome, centro_treinamento=atleta.centro_treinamento, categoria=atleta.categoria) for atleta in atletas]
    return atletas_out

@router.get(
        '/atleta/{id}', 
        summary='Consultar um atleta por id',
        status_code=status.HTTP_200_OK, 
        response_model=AtletaOut,
)
async def query_atleta_id(id: UUID4, db_session: DatabaseDependency) -> AtletaOut:
    atleta: CategoriaModel = (await db_session.execute(select(CategoriaModel).filter_by(id=id))).scalars().first()
    if not atleta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Atleta não encontrado no id:{id}')
    atleta_out = AtletaOut(nome=atleta.nome, centro_treinamento=atleta.centro_treinamento, categoria=atleta.categoria)
    return atleta_out