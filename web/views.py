from django.shortcuts import render


def index(request):
    context_dict = dict()

    return render(request, 'index.html', context_dict)
