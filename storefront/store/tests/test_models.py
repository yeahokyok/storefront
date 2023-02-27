import pytest

from .factories import ProductFactory

pytestmark = pytest.mark.django_db


def test_product_str():
    product = ProductFactory()
    assert str(product) == product.title
