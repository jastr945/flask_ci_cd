import api
import json
import pytest


@pytest.fixture
def client():
    api.app.config['TESTING'] = True
    client = api.app.test_client()
    yield client


def test_endpoint_message(client):
    rv = client.get('/')
    assert 'Endpoint success' in json.loads(rv.data)['msg']


def test_endpoint_status_code(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert rv.status_code != 400
