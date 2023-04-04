from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_predict_positive():
    response = client.post("/predict/",
                           json={"text": "I like machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'POSITIVE'


def test_predict_positive_2():
    response = client.post("/predict/",
                           json={"text": "I enjoy sport!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'POSITIVE'


def test_negative_sentiment_analysis_1():
    response_post = client.post("/predict/",
                                json={"text": "I hate machine learning!"})
    json_data = response_post.json()
    assert response_post.status_code == 200
    assert json_data['label'] == 'NEGATIVE'


def test_negative_sentiment_analysis_2():
    response_post = client.post("/predict/",
                                json={"text": "I don't like to drink milk!"})
    json_data = response_post.json()
    assert response_post.status_code == 200
    assert json_data['label'] == 'NEGATIVE'

