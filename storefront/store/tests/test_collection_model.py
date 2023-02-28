import pytest

from .factories import CollectionFactory, ProductFactory

pytestmark = pytest.mark.django_db


def test_collection_str():
    collection = CollectionFactory()
    assert str(collection) == collection.title
    assert collection.__str__() == collection.title


def test_collection_featured_product():
    product = ProductFactory()
    collection = CollectionFactory(featured_product=product)
    assert collection.featured_product == product
