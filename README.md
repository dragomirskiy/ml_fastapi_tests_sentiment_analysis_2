# 1. Приложение для определения тональности текста.

ПРАКТИЧЕСКОЕ ЗАДАНИЕ<br>по дисциплине "Программная инженерия" магистратуры "Инженерия машинного обучения" (2 семестр)<br>Уральского Федерального Университета. Работу выполнили студенты 1-курса:
- Драгомирский Радмил, группа: РИМ-120963
- Игорь Пластов, группа: РИМ-120963
- Дмитрий Шалагин, группа: РИМ-120963
- Агеев Николай Сергеевич, группа: РИМ-120963 

# 2. Запуск приложения.
Приложение состоит из 2-х частей:
- FastAPI -> файл `main.py`
- Streamlit -> файл `main_for_streamlit.py`

Соответственно есть 2 способа запустить приложение, описанные ниже.

## 2.1. Установка FastAPI.
Перед тем, как начать использовать библиотеку FastAPI, ее нужно установить. Делаем это с помощью команды:<br>
**`pip install fastapi`**<br><br>
Установка веб-сервера [Uvicorn](https://www.uvicorn.org/), в котором будет работать приложение, использующее FastAPI:<br>
**`pip install uvicorn`**
## 2.2. Первый запуск FastAPI.
Запуск приложения осуществляется средствами веб-сервера *Uvicorn*.
В каталоге, где находится файл main.py, запустите следующую команду:<br>
**`uvicorn main:app`**

Здесь:

- `uvicorn` — команда для запуска веб-сервер *Uvicorn.*
- `main` — название Python файла с приложением *FastAPI.*
- `app` — название переменной FastAPI из файла *main.py*

В случае успешного запуска вы получите следующее сообщение:<br>
<a href="https://ibb.co/J2T5TtR"><img src="https://i.ibb.co/sQ4y4Rv/10.png" alt="10" border="0"></a>

Сервер **Uvicorn** успешно запущен, указана ссылка, по которой он работает — *http://127.0.0.1:8000*<br>
<a href="https://ibb.co/PNK41mb"><img src="https://i.ibb.co/MsrpP2j/11.png" alt="11" border="0"></a>

## 2.3. Запуск средствами Streamlit.

Установка Streamlit с помощью pip:<br>
**`pip install streamlit`**<br>

Запуск Web-приложения выполняется командой:<br>
**`streamlit run app.py`**<br>

При запуске нужно указать имя скрипта на Python с описанием Web-страницы, в данном примере **app.py**. Streamlit запустит встроенный Web-сервер, а в нем — страницу на основе скрипта app.py:<br><br>
<a href="https://ibb.co/V3Gj0P3"><img src="https://i.ibb.co/st4mpMt/20.png" alt="20" border="0"></a>

# 3. Использование приложения.
## 3.1. Инструменты для работы с API: `curl`.
Запрос с помощью curl:

```
curl -X 'POST' \
  'http://127.0.0.1:8000/predict/' \
  -H 'Content-Type: application/json' \
  -d {
  "text": "I hate machine learning engineering!"
}
```

В этом запросе используются следующие компоненты:

- ***-X 'POST'*** — параметр, который указывает curl использовать метод POST HTTP.
- ***http://127.0.0.1:8000/predict/*** — адрес метода API.
- ***H 'Content-Type: application/json'*** — параметр, который устанавливает заголовок, определяющий тип тела запроса (application/json).
- ***d '{ "text": "I hate machine learning engineering!"}'*** — данные для тела запроса в формате JSON. Данные содержат одно поле, заголовок "text" (именно этот заголовок указан в модели pydantic в нашем коде), значение  "I hate machine learning engineering!".

Так выглядит результат выполнения команды `curl` в терминале:

<a href="https://ibb.co/Fnn15dL"><img src="https://i.ibb.co/TrrG4Nx/image.png" alt="image" border="0"></a>

## 3.2. Инструменты для работы с API: `Postman`
### 3.2.1. Установка Postman.
1. Чтобы установить Postman на свой компьютер, перейдите по [ссылке](https://www.postman.com/downloads/).
2. Скачайте версию Postman для своей операционной системы.
3. После скачивания запустите установочный файл и выполните установку.

Также существует **веб-версия Postman**, которую можно использовать, не устанавливая на свой компьютер. Веб-версия доступна [здесь](https://identity.getpostman.com/login?continue=https%3A%2F%2Fweb.postman.co%2F).

### 3.2.1. Работа с API Postman.
При запуске Postman вы попадаете в свое рабочее пространство (**My Workspace**).<br>
<a href="https://ibb.co/G3kL0LH"><img src="https://i.ibb.co/M5p4s4B/1.png" alt="1" border="0"></a>

Чтобы создать запрос к API, нужно нажать на кнопку + в верхней панели рабочего пространства.<br> 
<a href="https://ibb.co/ckH8QVR"><img src="https://i.ibb.co/q7fgpVh/2.png" alt="2" border="0"></a>

Откроется окно для ввода запроса к API.<br>
<a href="https://ibb.co/ZHgXRf5"><img src="https://i.ibb.co/k3DBVGj/3.png" alt="3" border="0"></a>

Для запуска запроса нужно вставить ссылку в поле *«Enter request URL»* и нажать кнопку *«Send»*. <br>
<a href="https://ibb.co/nRWn9Qm"><img src="https://i.ibb.co/g6nPNt9/4.png" alt="4" border="0"></a>

Результат выполнения запроса будет показан в нижней части экрана окна Postman<br>
<a href="https://ibb.co/C9tb36Z"><img src="https://i.ibb.co/wQLSF7X/5.png" alt="5" border="0"></a>

Параметры в Postman указываются в таблице под ссылкой для запроса. Вот пример указания параметра ***lang=ru***.  Сервер возвращает данные на русском языке.<br>
<a href="https://ibb.co/Mgb8gSy"><img src="https://i.ibb.co/K5YN5hc/6.png" alt="6" border="0"></a>

Метод HTTP в Postman выбирается слева от URL. Список доступных методов достаточно большой, но, помимо **GET** и **POST**, другие методы почти не используются.<br>
<a href="https://ibb.co/HgcbqDt"><img src="https://i.ibb.co/h8G4VRB/7.png" alt="7" border="0"></a>

Статус выполнения запроса HTTP показывается в правой верхней части окна результатов запроса. Если подвести мышь к статусу, то появится подсказка с описанием, что он означает.<br>
<a href="https://ibb.co/C22W3f6"><img src="https://i.ibb.co/GTTF4q9/8.png" alt="8" border="0"></a>

Заголовки в Postman можно задать, если переключить таблицу под URL на вкладку Headers.<br>
<a href="https://ibb.co/4jXzxKr"><img src="https://i.ibb.co/CnYgFmG/9.png" alt="9" border="0"></a>


# 4. Используемые библиотеки.
Определение тональности текста осуществляется **ТОЛЬКО** на английском языке с помощью библиотеки Hugging Face.<br>
Для тестирования API используется инструмент TestClient из FastAPI.<br>
Для создания WEB-приложения используется Streamlit.

Перечень всех необходимых библиотек = requirements:
- fastapi
- uvicorn
- transformers
- torch
- httpx
- streamlit
- tensorflow
- tensorflow-cpu
