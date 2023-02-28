import pytest

from django.db import IntegrityError
from django.core.exceptions import ValidationError

from ..models import Customer
from .factories import CustomerFactory, OrderFactory

pytestmark = pytest.mark.django_db


def test_customer_first_name():
    customer = CustomerFactory()
    assert customer.first_name


def test_customer_last_name():
    customer = CustomerFactory()
    assert customer.last_name


def test_customer_email():
    customer = CustomerFactory()
    assert customer.email


def test_customer_email_unique():
    customer = CustomerFactory()
    with pytest.raises(IntegrityError):
        CustomerFactory(email=customer.email)


def test_customer_phone():
    customer = CustomerFactory()
    assert customer.phone


def test_customer_membership_choices():
    customer = CustomerFactory()
    assert customer.membership in ["B", "S", "G"]


def test_customer_membership_default():
    customer = Customer.objects.create(
        first_name="John", last_name="Doe", email="mail@mail.com", phone="123"
    )
    assert customer.membership == "B"


def test_customer_str():
    customer = CustomerFactory()
    assert str(customer) == f"{customer.first_name} {customer.last_name}"


def test_customer_order():
    customer = CustomerFactory()
    order = OrderFactory(customer=customer)
    assert customer.orders.first() == order
