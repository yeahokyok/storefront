import pytest

from .factories import OrderFactory, CustomerFactory
from ..models import Order

pytestmark = pytest.mark.django_db


def test_order_customer():
    customer = CustomerFactory()
    order = OrderFactory(customer=customer)
    assert order.customer == customer


def test_order_placed_at():
    order = OrderFactory()
    assert order.placed_at


def test_order_payment_status_choices():
    order = OrderFactory()
    assert order.payment_status in ["P", "C", "F"]


def test_order_payment_status_default():
    customer = CustomerFactory()
    order = Order.objects.create(customer=customer)
    assert order.payment_status == "P"
