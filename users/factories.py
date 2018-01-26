import factory


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker('email')

    class Meta:
        model = 'users.User'
