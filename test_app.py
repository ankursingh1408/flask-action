import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'
    assert 'Welcome' in data['message']


def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'


def test_greet(client):
    response = client.get('/api/greet/World')
    assert response.status_code == 200
    data = response.get_json()
    assert data['greeting'] == 'Hello, World!'
    assert data['status'] == 'success'
