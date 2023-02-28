import pytest

from .factories import OrderFactory, OrderItemFactory, ProductFactory

pytestmark = pytest.mark.django_db


def test_order_item_order():
    order = OrderFactory()
    order_item = OrderItemFactory(order=order)
    assert order_item.order == order


def test_order_item_product():
    product = ProductFactory()
    order_item = OrderItemFactory(product=product)
    assert order_item.product == product


def test_order_item_quantity():
    order_item = OrderItemFactory()
    assert order_item.quantity > 0


def test_order_item_unit_price():
    order_item = OrderItemFactory()
    assert order_item.unit_price > 0
