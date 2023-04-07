from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

from .models import Projects, Language, Suggestions


def response_language(request, language: str):
    if language == 'all':
        redirect_url = reverse('all_languages_path', args=[])
        return HttpResponseRedirect(redirect_url)
    elif language.capitalize() in [lang.name for lang in Language.objects.all()]:

        language_model = Language.objects.filter(name=language.capitalize())[0]
        project_models = Projects.objects.filter(language_id=language_model.id)

        context = {
            'language': language_model,
            'projects': project_models
        }

        return render(request, 'portfolio/one_lang.html', context=context)

    return HttpResponseNotFound(f'Unknown language - {language}')


def response_languages_by_number(request, language_number: int):
    if language_number > len(Language.objects):
        return HttpResponseNotFound(f'Unknown language number ({len(Language.objects)} max) - {language_number}')

    language = Language.objects[language_number - 1]
    redirect_url = reverse('portfolio_path', args=[language.name])
    return HttpResponseRedirect(redirect_url)


def response_all_languages(request):
    projects = {language: [project for project in Projects.objects.filter(language_id=language.id).all()] for
                language in Language.objects.all()}
    context = {
        'projects': projects
    }

    return render(request, 'portfolio/all_langs.html', context=context)


def response_about(request):
    return render(request, 'portfolio/about.html')


def redirect_lower(request):
    redirect_url = reverse('portfolio_path', args=['all'])
    return HttpResponseRedirect(redirect_url)


def response_suggestion(request):
    if request.POST or request.GET:
        if "delete" not in request.GET:
            new_suggestor = Suggestions()
            new_suggestor.name = request.POST["name"]
            new_suggestor.surname = request.POST["surname"]
            new_suggestor.phone_number = request.POST["phone"]
            new_suggestor.comment = request.POST["com"]
            new_suggestor.save()
        elif "delete" in request.GET and request.GET["delete"] == "delete":
            deletable_suggestion = Suggestions.objects.get(id=request.GET["id"])
            deletable_suggestion.delete()
    suggestions = list(Suggestions.objects.all())
    context = {
        'suggestions': suggestions,
        'closable_number': request.POST["phone"] if request.POST else -1
    }
    return render(request, 'portfolio/suggestions.html', context=context)
