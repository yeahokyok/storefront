import factory

from ..models import Product, Promotion, Collection


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    title = factory.Sequence(lambda n: f"Product {n}")
    description = factory.Faker("text", max_nb_chars=200)
    price = factory.Faker("pydecimal", left_digits=2, right_digits=2, positive=True)
    inventory = factory.Faker("pyint", min_value=0, max_value=1000)
    last_updated = factory.Faker("date_time_this_year")


class PromotionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Promotion

    description = factory.Faker("text", max_nb_chars=200)
    discount = factory.Faker("pydecimal", left_digits=2, right_digits=2, positive=True)


class CollectionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Collection

    title = factory.Sequence(lambda n: f"Collection {n}")
    featured_product = factory.SubFactory(ProductFactory)
