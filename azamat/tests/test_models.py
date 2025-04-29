import pytest
from azamat.models import Product

def test_product_str():
    product = Product(name="Test product")
    assert str(product) == "Test product"