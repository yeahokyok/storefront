import pytest

from .factories import ProductFactory, PromotionFactory

pytestmark = pytest.mark.django_db


def test_promotion_description():
    promotion = PromotionFactory(description="test")
    assert promotion.description == "test"


def test_promotion_discount():
    promotion = PromotionFactory(discount=11.22)
    assert promotion.discount == 11.22


def test_promotion_products():
    promotion = PromotionFactory()
    promotion.products.add(ProductFactory())
    promotion.products.add(ProductFactory())
    assert promotion.products.count() == 2
