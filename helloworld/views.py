import datetime

from django.shortcuts import render

from .models import Counter
from .forms import HelloWorldForm


def index(request):
    # retriever counter model instance from DB or create it if it doesn't exist yet
    counter, created = Counter.objects.get_or_create(name='hello-world-button')

    # increment counter when a POST request arrives (from the button click)
    if request.method == 'POST':
        counter.value += 1
        counter.save()

        # and get the values filled in form
        form = HelloWorldForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            date = form.cleaned_data['date']

    else:
        form = HelloWorldForm()
        username = 'Nobody'
        date = datetime.date.today()

    context = {
        'clicks': counter.value,
        'form': form,
        'username': username,
        'date': date,
    }
    return render(request, 'helloworld/index.html', context)
