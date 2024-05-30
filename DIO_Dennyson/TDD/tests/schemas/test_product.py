
from uuid import UUID

from pydantic import ValidationError
import pytest
from store.schemas.product import ProductIn
from tests.schemas.factories import product_data

def test_schemas_return_success():
    data =  product_data()
    product = ProductIn.model_validate(data)
    assert product.name == "Iphone 15"
    assert isinstance(product.id, UUID)

def test_schemas_return_raise():
    data = {'name':"Iphone 15", 'quantity':20, 'price':14.000}

    with pytest.raises(ValidationError) as erro:
        ProductIn.model_validate(data)
