# Подключим TestClient — клиент для тестрования API из FastAPI.
from fastapi.testclient import TestClient

# Импортируем объект app класса FastAPI из файл main.py в текущем каталоге.
# В файле main.py содержится код приложения API для модели машинного обучения.
from main import app

# Создание клиента для тестирования, которому при создании передается объект API app
client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_positive_sentiment_analysis_1():
    response_post = client.post("/predict/",
                                json={"text": "I like machine learning!"})
    json_data = response_post.json()
    assert response_post.status_code == 200
    assert json_data['label'] == 'POSITIVE'


def test_positive_sentiment_analysis_2():
    response_post = client.post("/predict/",
                                json={"text": "I enjoy sport!"})
    json_data = response_post.json()
    assert response_post.status_code == 200
    assert json_data['label'] == 'POSITIVE'

# Проверяет тональность отрицательной фразы.
def test_negative_sentiment_analysis_1():
    # Клиент передает запрос POST, путь на сервере "/predict/".
    # В теле сообщения в формате JSON передается сообщение для определения тональности.
    response_post = client.post("/predict/",
                                json={"text": "I hate machine learning!"})
    # Тело ответа из формата JSON в виде словаря сохраняется в переменную json_data для последующего анализа.
    json_data = response_post.json()
    # Проверяет доступность приложения. Код статуса ответа HTTP должен быть равен 200.
    assert response_post.status_code == 200
    # Проверяет результат распознавания. Тональность фразы положительная, поэтому
    # результат определения тональности (ключ 'label' в словаре json_data) должен быть 'NEGATIVE'.
    assert json_data['label'] == 'NEGATIVE'


def test_negative_sentiment_analysis_2():
    response_post = client.post("/predict/",
                                json={"text": "I don't like to drink milk!"})
    json_data = response_post.json()
    assert response_post.status_code == 200
    assert json_data['label'] == 'NEGATIVE'
