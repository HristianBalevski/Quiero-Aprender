from .services import translate_with_mymemory
import json

from django.shortcuts import redirect
from .services import delete_flashcard, create_flashcard, save_flashcard
from django.shortcuts import render

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



def flashcard_view(request):
    text = request.GET.get('text', '')
    flashcard = None
    error_message = None

    if text:
        try:

            flashcard = create_flashcard(text, from_lang="en", to_lang="es")
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
    if delete_flashcard(index):
        return redirect('view_flashcards')
    else:
        return redirect('view_flashcards')






