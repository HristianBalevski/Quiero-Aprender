
from django.shortcuts import render
from .services import translate_with_mymemory
import json

from django.shortcuts import redirect
from .services import delete_flashcard
def translate_view(request):
    text = request.GET.get('text', '')
    translation = None
    error_message = None

    if text:
        try:
            translation = translate_with_mymemory(text)
        except Exception as e:
            error_message = str(e)

    context = {
        'text': text,
        'translation': translation,
        'error_message': error_message
    }
    return render(request, 'lessons/api-translator.html', context)



from django.shortcuts import render
from .services import create_flashcard, save_flashcard  # Импортираме функциите

def flashcard_view(request):
    text = request.GET.get('text', '')  # Вземаме текста от заявката
    flashcard = None
    error_message = None

    if text:
        try:
            # Създаваме флаш карта
            flashcard = create_flashcard(text, from_lang="en", to_lang="es")
            # Запазваме я в JSON файл
            save_flashcard(flashcard)
        except Exception as e:
            error_message = str(e)

    context = {
        'text': text,
        'flashcard': flashcard,
        'error_message': error_message
    }
    return render(request, 'lessons/flashcard.html', context)


def view_flashcards(request):
    try:
        with open("flashcards.json", "r") as file:
            flashcards = json.load(file)
    except FileNotFoundError:
        flashcards = []

    return render(request, 'lessons/view_flashcards.html', {'flashcards': flashcards})


def delete_flashcard_view(request, index):
    """
    View за изтриване на флаш карта.
    """
    if delete_flashcard(index):
        return redirect('view_flashcards')  # Редирект към списъка с флаш карти
    else:
        return redirect('view_flashcards')  # Редирект при грешка






