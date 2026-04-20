import pytest
import requests

URL = "https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&current_weather=true"

@pytest.fixture(scope="session")
def response():
    return requests.get(URL, timeout=2)

@pytest.fixture(scope="session")
def data(response):
    return response.json()

def test_status_code(response):
    assert response.status_code == 200

def test_response_time(response):
    assert response.elapsed.total_seconds() < 1.5

def test_json_structure(data):
    assert "current_weather" in data

def test_temperature_value(data):
    assert isinstance(data["current_weather"]["temperature"], (int, float))

def test_temperature_range(data):
    temp = data["current_weather"]["temperature"]
    assert -50 < temp < 60

def test_wind_speed_present(data):
    assert "windspeed" in data["current_weather"]

def test_time_field_exists(data):
    assert "time" in data["current_weather"]

def test_invalid_endpoint():
    bad_url = "https://api.open-meteo.com/invalid"
    response = requests.get(bad_url)
    assert response.status_code != 200