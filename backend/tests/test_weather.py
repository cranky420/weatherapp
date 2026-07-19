from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_weather_endpoint_returns_json():
    response = client.get('/weather?city=Kolkata')
    assert response.status_code == 200
    data = response.json()
    assert 'city' in data
    assert 'temperature' in data
    assert 'condition' in data
