import pytest

from .factories import CartFactory, CartItemFactory, ProductFactory

pytestmark = pytest.mark.django_db


def test_cart_item_cart():
    cart = CartFactory()
    cart_item = CartItemFactory(cart=cart)
    assert cart_item.cart == cart


def test_cart_item_product():
    product = ProductFactory()
    cart_item = CartItemFactory(product=product)
    assert cart_item.product == product


def test_cart_item_quantity():
    cart_item = CartItemFactory()
    assert cart_item.quantity


def test_cart_item_str():
    cart_item = CartItemFactory()
    assert (
        str(cart_item)
        == f"{cart_item.quantity} of {cart_item.product} in cart {cart_item.cart}"
    )
