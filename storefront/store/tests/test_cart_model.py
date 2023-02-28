import pytest

from .factories import CartFactory

pytestmark = pytest.mark.django_db


def test_cart_created_at():
    cart = CartFactory()
    assert cart.created_at


def test_cart_str():
    cart = CartFactory()
    assert str(cart) == f"Cart {cart.id}"
