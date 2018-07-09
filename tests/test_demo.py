import requests

def test_demo():
    response = requests.get('http://0.0.0.0:8000/')
    assert (response.status_code == 200)
