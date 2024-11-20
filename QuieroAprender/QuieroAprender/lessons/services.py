import requests
import json


def translate_with_mymemory(text, from_lang="en", to_lang="es"):
    url = "https://api.mymemory.translated.net/get"
    params = {
        "q": text,
        "langpair": f"{from_lang}|{to_lang}"
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get("responseData", {}).get("translatedText", "No translation available")
    else:
        return f"Error: {response.status_code} - {response.text}"


def create_flashcard(front, from_lang="en", to_lang="es"):
    # Генерираме превод с MyMemory API
    translated_text = translate_with_mymemory(front, from_lang, to_lang)
    # Връщаме флаш карта като речник
    return {
        "Front": front,
        "Back": translated_text
    }




def save_flashcard(flashcard, file_path="flashcards.json"):
    try:
        # Опитваме се да заредим съществуващите карти
        with open(file_path, "r") as file:
            flashcards = json.load(file)
    except FileNotFoundError:
        # Ако файлът не съществува, започваме със списък
        flashcards = []

    # Добавяме новата карта
    flashcards.append(flashcard)

    # Запазваме обратно във файла
    with open(file_path, "w") as file:
        json.dump(flashcards, file, indent=4)


def delete_flashcard(index, file_path="flashcards.json"):
    """
    Изтрива флаш карта по индекс от JSON файла.
    """
    try:
        # Четем текущите карти
        with open(file_path, "r") as file:
            flashcards = json.load(file)

        # Проверяваме дали индексът е валиден
        if 0 <= index < len(flashcards):
            del flashcards[index]  # Изтриваме картата
            # Записваме обратно
            with open(file_path, "w") as file:
                json.dump(flashcards, file, indent=4)
            return True
        else:
            return False
    except FileNotFoundError:
        return False




