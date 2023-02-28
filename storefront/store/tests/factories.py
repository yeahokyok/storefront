import factory

from ..models import Product, Promotion, Collection, Customer, Order, OrderItem


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


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    phone = factory.Faker("phone_number")
    membership = factory.Faker("random_element", elements=("B", "S", "G"))


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    customer = factory.SubFactory(CustomerFactory)
    placed_at = factory.Faker("date_time_this_year")
    payment_status = factory.Faker("random_element", elements=("P", "C", "F"))


class OrderItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OrderItem

    order = factory.SubFactory(OrderFactory)
    product = factory.SubFactory(ProductFactory)
    quantity = factory.Faker("pyint", min_value=1, max_value=10)
    unit_price = factory.Faker(
        "pydecimal", left_digits=2, right_digits=2, positive=True
    )
