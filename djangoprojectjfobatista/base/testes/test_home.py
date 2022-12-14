import pytest

from django.urls import reverse

from djangoprojectjfobatista.django_assertions import assert_contains


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title> Home - Cards </title>')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}">Django</a>')


def test_email_link(resp):
    assert_contains(resp, '<a href="mailto:jfobatista@hotmail.com')

