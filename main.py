import streamlit as st

# алфавит
ENCRYPT_DICT = {
    'а': '1!', 'б': '2@', 'в': '3#', 'г': '4$', 'д': '5%',
    'е': '6^', 'ё': '7&', 'ж': '8*', 'з': '9(', 'и': '0)',
    'й': '1_', 'к': '2+', 'л': '3-', 'м': '4=', 'н': '5[',
    'о': '6]', 'п': '7{', 'р': '8}', 'с': '9|', 'т': '0:',
    'у': '1;', 'ф': '2"', 'х': "3'", 'ц': '4<', 'ч': '5>',
    'ш': '6,', 'щ': '7.', 'ъ': '8?', 'ы': '9/', 'ь': '0~',
    'э': '1`', 'ю': '2!', 'я': '3@'
}
# Обратный словарь для дешифровки
DECRYPT_DICT = {v: k for k, v in ENCRYPT_DICT.items()}


# ===Шифрование===
def encrypt_text(text: str) -> str:
    """Преобразует русский текст в шифр (цифры + знаки)."""
    result = []
    for ch in text:
        lower_ch = ch.lower()
        if lower_ch in ENCRYPT_DICT:
            result.append(ENCRYPT_DICT[lower_ch])
        else:

            result.append(ch)
    return ''.join(result)


def decrypt_text(cipher: str) -> str:
    """Расшифровывает последовательность цифр+знаков обратно в русский текст."""
    result = []
    i = 0
    while i < len(cipher):

        if (i + 1 < len(cipher) and
                cipher[i].isdigit() and
                not cipher[i + 1].isalnum()):
            pair = cipher[i:i + 2]
            if pair in DECRYPT_DICT:
                result.append(DECRYPT_DICT[pair])
                i += 2
                continue

        result.append(cipher[i])
        i += 1
    return ''.join(result)


# ===Крутой интерфейс===
st.set_page_config(
    page_title="Шифратор «ЦифроЗнак»",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Шифратор русского текста в цифры и знаки")
st.markdown("Каждая русская буква заменяется уникальной парой **цифра + спецсимвол**.")


mode = st.radio(
    "Выберите действие:",
    ["🔒 Зашифровать", "🔓 Расшифровать"],
    horizontal=True
)


input_text = st.text_area(
    "Введите текст:",
    height=150,
    placeholder="Например: Привет, мир!"
)

#кнопка выполнить
if st.button("Выполнить", type="primary"):
    if not input_text.strip():
        st.warning("Введите текст для обработки.")
    else:
        if mode == "🔒 Зашифровать":
            result = encrypt_text(input_text)
            st.success("Текст успешно зашифрован:")
            st.code(result, language="text")
        else:
            result = decrypt_text(input_text)
            st.success("Текст успешно расшифрован:")
            st.code(result, language="text")

#панелька шифра
with st.sidebar:
    st.header("📖 Таблица соответствия")
    st.caption("Буква → Код (цифра + знак)")

    # Разбиваем словарь на две колонки для компактности
    items = list(ENCRYPT_DICT.items())
    col1, col2 = st.columns(2)

    half = len(items) // 2 + len(items) % 2
    with col1:
        for letter, code in items[:half]:
            st.markdown(f"**{letter}** → `{code}`")
    with col2:
        for letter, code in items[half:]:
            st.markdown(f"**{letter}** → `{code}`")

    st.divider()
    st.caption("💡 Пробелы, цифры и знаки препинания остаются без изменений.")