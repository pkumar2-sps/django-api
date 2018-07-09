import requests

def test_demo():
    response1 = requests.get('http://127.0.0.1:8000/')
    response2 = requests.get('http://localhost:8000/')
    assert (response1 == response2)
