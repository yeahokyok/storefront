import pytest

from django.db import IntegrityError

from .factories import ProductFactory, PromotionFactory

pytestmark = pytest.mark.django_db


def test_product_str():
    product = ProductFactory()
    assert str(product) == product.title
    assert product.__str__() == product.title


def test_product_description():
    product = ProductFactory(description="test")
    assert product.description == "test"


def test_product_price():
    product = ProductFactory(price=11.22)
    assert product.price == 11.22


def test_product_price():
    product = ProductFactory(price=10)
    assert product.price == 10


# Django validation is not validating at database level so it is not validating on save
# def test_product_neg_price():
#     with pytest.raises(ValidationError):
#         ProductFactory(price=-10)


def test_product_inventory():
    product = ProductFactory(inventory=123)
    assert product.inventory == 123


def test_product_neg_inventory():
    with pytest.raises(IntegrityError):
        ProductFactory(inventory=-10)


def test_product_promotions():
    product = ProductFactory()
    product.promotions.add(PromotionFactory())
    product.promotions.add(PromotionFactory())
    assert product.promotions.count() == 2
