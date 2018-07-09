import requests

def test_demo():
    response = requests.get('http://localhost:8000/')
    assert (response.status_code == 200)
