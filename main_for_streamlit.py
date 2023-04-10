from transformers import pipeline
import streamlit as st


# Создаем и возвращаем пайплайн для определения тональности текста.
def get_pipeline():
    qa = pipeline('sentiment-analysis')
    return qa


def sentiment_and_score(inputs):
    qa = get_pipeline()
    # Значения context получаем из поля ввода (создается средствами streamlit).
    result = qa(inputs)[0]

    # Возвращаем кортеж с результатами:
    # первый элемент - это собственно предполагаемая тональность текста,
    # а второй элемент - оценка (score)
    return result['label'], result['score']


# if __name__ == '__main__':
#     try:
#         # Определение тональности текста.
#         st.title('ОПРЕДЕЛЕНИЕ ТОНАЛЬНОСТИ ТЕКСТА.')
#         # Поле ввода текста. value - значение по умолчанию.
#         context = st.text_input('CONTEXT:', value='I love this beautiful world!')
#         # Кнопка, нажатие на которую запускает процесс определения тональности.
#         result = st.button('ОПРЕДЕЛИТЬ ТОНАЛЬНОСТЬ')
#         if result:
#             # Моя функция sentiment_and_score возвращает кортеж, в котором первый элемент
#             # собственно тональность, а второй - оценка (score) =>
#             # в следующей строке делаем распаковку кортежа, и вывод результатов.
#             label, score = sentiment_and_score(context)
#             st.text(f'LABEL={label}\nSCORE={score}')
#     except ValueError:
#         st.text('ЗАПОЛНИТЕ ПОЛЕ ВВОДА!')

if __name__ == '__main__':
    try:
        # Определение тональности текста.
        st.title('ОПРЕДЕЛЕНИЕ ТОНАЛЬНОСТИ ТЕКСТА.')
        # Поле ввода текста. value - значение по умолчанию.
        context = st.text_input('CONTEXT:', value='I love this beautiful world!')
        # Кнопка, нажатие на которую запускает процесс определения тональности.
        result = st.button('ОПРЕДЕЛИТЬ ТОНАЛЬНОСТЬ')
        if context:
            # Моя функция sentiment_and_score возвращает кортеж, в котором первый элемент
            # собственно тональность, а второй - оценка (score) =>
            # в следующей строке делаем распаковку кортежа, и вывод результатов.
            label, score = sentiment_and_score(context)
            st.text(f'LABEL={label}\nSCORE={score}')
        else:
            raise ValueError('Пустое поле ввода.')
    except ValueError:
        st.text('ЗАПОЛНИТЕ ПОЛЕ ВВОДА!')
