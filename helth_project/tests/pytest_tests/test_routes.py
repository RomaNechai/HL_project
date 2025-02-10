import pytest

from http import HTTPStatus

from django.urls import reverse


def test_home_availability_for_anonymous_user(client):
    url = reverse('posts:index_list')
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.parametrize(
    'name',
    ('posts:index_list', 'posts:group_list', 'users:signup')
)
def test_pages_availability_for_anonymous_user(client, name):
    url = reverse(name)
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK

def test_ex():
    assert 1 == 1