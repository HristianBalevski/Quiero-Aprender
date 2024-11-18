import requests

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



