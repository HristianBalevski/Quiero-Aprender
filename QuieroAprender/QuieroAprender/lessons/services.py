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
    translated_text = translate_with_mymemory(front, from_lang, to_lang)
    return {
        "Front": front,
        "Back": translated_text
    }

def save_flashcard(flashcard, user_id, file_path_template="flashcards_{user_id}.json"):

    file_path = file_path_template.format(user_id=user_id)

    try:

        with open(file_path, "r") as file:
            flashcards = json.load(file)
    except FileNotFoundError:

        flashcards = []


    flashcards.append(flashcard)


    with open(file_path, "w") as file:
        json.dump(flashcards, file, indent=4)


def delete_flashcard(index, user_id, file_path_template="flashcards_{user_id}.json"):

    file_path = file_path_template.format(user_id=user_id)

    try:

        with open(file_path, "r") as file:
            flashcards = json.load(file)

        if 0 <= index < len(flashcards):
            del flashcards[index]

            with open(file_path, "w") as file:
                json.dump(flashcards, file, indent=4)
            return True
        else:
            return False
    except FileNotFoundError:
        return False











