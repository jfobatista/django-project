import pytest
from django.urls import reverse

from djangoprojectjfobatista.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:video', args=('bituca',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_title_video(resp):
    assert_contains(resp, '<h1 class="card-header"> Bituquinha </h1>')


def test_conteudo_video(resp):
    assert_contains(resp, '<iframe src="https://player.vimeo.com/video/770026394?h=d7374aab3a&amp;badge=0'
                          '&amp;autopause=0&amp;player_id=0&amp;app_id=58479" ')


