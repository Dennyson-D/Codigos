from typing import List
from uuid import UUID

import pytest
from store.core.exceptions import NotFoundException
from store.schemas.product import ProductOut, ProductUpdateOut
from store.usecases.product import product_usecase

async def test_usecases_should_return_success(product_in):
    result = await product_usecase.create(body=product_in())

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 15"

async def test_usecases_get_return_success(product_inserted):
    result = await product_usecase.get(id=product_inserted.id)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 15"    

async def test_usecases_should_not_found():
    with pytest.raises(Exception) as err:
        await product_usecase.get(id=UUID('123abc'))    

    assert err.message == "Product not found with filter: UUID('123abc')"    

async def test_usecases_query_should_return_success():    
    result = await product_usecase.query()

    assert isinstance(result,List)

async def test_usecases_update_should_return_success(product_id,product_up):  
    product_up.price = "7.500"
    result = await product_usecase.update(id=product_id, body=product_up)

    assert isinstance(result, ProductUpdateOut)

async def test_usecases_delete_should_return_success(product_id):   
    result = await product_usecase.delete(id=product_id)

    assert result is True

async def test_usecases_delete_should_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecase.delete(id=UUID('123abc'))    

    assert err.value.message == "Product not found with filter: '123abc'"      