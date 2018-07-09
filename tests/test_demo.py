import requests

def test_demo():
    response = requests.get('http://0.0.0.0:8000/' + "api/v1/reports/1")
    assert (response.status_code == 200)
