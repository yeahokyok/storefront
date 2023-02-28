import pytest

from .factories import AddressFactory, CustomerFactory


pytestmark = pytest.mark.django_db


def test_address_customer():
    customer = CustomerFactory()
    address = AddressFactory(customer=customer)
    assert address.customer == customer


def test_address_street():
    address = AddressFactory()
    assert address.street


def test_address_city():
    address = AddressFactory()
    assert address.city


def test_address_str():
    address = AddressFactory()
    assert str(address) == f"{address.street}, {address.city} of {address.customer}"
