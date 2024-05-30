from typing import List
from urllib import response

import pytest
from tests.conftest import products_url
from tests.schemas.factories import product_data
from fastapi import status

async def test_controller_create_should_return_success(client, products_url):
    response = await client.post(products_url, json=product_data())

    content = response.josn()
    del content['created_at']
    del content['updated_at']
    del content['id']

    assert response.status_code == status.HTTP_201_CREATED

async def test_controller_get_should_return_success(client, products_url, product_inserted):
    response = await client.get(f"{products_url}{product_inserted.id}")

    assert response.status_code == status.HTTP_201_CREATED   

@pytest.mark.usefixtures("products_inserted")
async def test_controller_query_should_return_success(client, product_url):
    response = await client.get(products_url)  

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), List)  
    assert len(response.joson) > 1

async def test_controller_patch_should_return_success(client, products_url, product_inserted):
    response = await client.get(f"{products_url}{product_inserted.id}", json={"quantity":50})

    assert response.status_code == status.HTTP_200_OK

async def test_controller_delete_should_return_success(client, products_url, product_inserted):
    response = await client.get(f"{products_url}{product_inserted.id}")

    assert response.status_code == status.HTTP_204_NO_CONTENT


