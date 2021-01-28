from django.shortcuts import render

from .models import Counter


def index(request):
    # retriever counter model instance from DB or create it if it doesn't exist yet
    counter, created = Counter.objects.get_or_create(name='hello-world-button')

    # increment counter when a POST request arrives (from the button click)
    if request.method == 'POST':
        counter.value += 1
        counter.save()

    context = {
        'clicks': counter.value,
    }
    return render(request, 'helloworld/index.html', context)
