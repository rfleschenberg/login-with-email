import pytest

from . import models
from .factories import UserFactory


@pytest.mark.django_db
def test_create_user():
    manager = models.User.objects
    manager.create_user('karl@example.org')
    user = models.User.objects.get(email='karl@example.org')
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser


@pytest.mark.django_db
def test_create_user_with_password():
    manager = models.User.objects
    manager.create_user('karl@example.org', password='insecure')
    user = models.User.objects.get(email='karl@example.org')
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser
    assert user.check_password('insecure')
    assert not user.check_password('wrong')


@pytest.mark.django_db
def test_create_user_with_invalid_email():
    manager = models.User.objects
    with pytest.raises(ValueError):
        manager.create_user('')


@pytest.mark.django_db
def test_create_superuser():
    manager = models.User.objects
    manager.create_superuser('karl@example.org', password='insecure')
    user = models.User.objects.get(email='karl@example.org')
    assert user.is_active
    assert user.is_staff
    assert user.is_superuser
    assert user.check_password('insecure')
    assert not user.check_password('wrong')


@pytest.mark.django_db
def test_create_superuser_without_is_staff():
    manager = models.User.objects
    with pytest.raises(ValueError):
        manager.create_superuser('karl@example.org', password='insecure',
                                 is_staff=False)


@pytest.mark.django_db
def test_create_superuser_without_is_superuser():
    manager = models.User.objects
    with pytest.raises(ValueError):
        manager.create_superuser('karl@example.org', password='insecure',
                                 is_superuser=False)


def test_get_full_name():
    user = models.User(email='karla@example.org')
    assert user.get_full_name() == 'karla@example.org'


def test_get_short_name():
    user = UserFactory.build(email='karla@example.org')
    assert user.get_short_name() == 'karla@example.org'
