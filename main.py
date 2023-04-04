# Подключаем класс FastAPI из библиотеки fastapi.
from fastapi import FastAPI
# Подключаем класс pipeline из модуля transformers библиотеки Hugging Face
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    text: str


# Создается объект FastAPI и классификатор из библиотеки Hugging Face на основе
# пайплайна с типом “sentiment-analysis”.
app = FastAPI()
classifier = pipeline("sentiment-analysis")


# Определим декоратор @app.get("/")
@app.get("/")
# Возвращает сообщение, которое мы хотим передать в формате
# JSON {"message": "Hello World"}
def root():
    return {"message": "Hello World"}


# Определим декоратор @app.post("/predict/")
@app.post("/predict/")
# Функция predict используется для реализации метода API — predict
def predict(item: Item):
    """Реализация метода API — predict.

    Args:
        item (Item): объект item типа Item (класс для наших данных на основе базовой модели из pydantic).

    Returns:
        dict: классификатор вызывается для поля text объекта item,
            который берется из параметра запроса HTTP к серверу.
            Результат работы классификатора (в данном случае - нулевой элемент списка)
            возвращается из функции.
    """
    # Вызов классификатора
    return classifier(item.text)[0]
