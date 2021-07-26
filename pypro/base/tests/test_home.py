from django.test import Client


def test_status_code9(client: Client):
    resp = client.get('/')
    assert resp.status_code == 200
