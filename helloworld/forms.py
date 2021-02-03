import datetime

from django import forms


class HelloWorldForm(forms.Form):
    """Form asking for the user's name and an arbitrary date, both used inside the displayed 'Hello World' text."""
    username = forms.CharField(label='Your name', max_length=100)
    date = forms.DateField(label='An arbitrary date', initial=datetime.date.today,
                           widget=forms.widgets.DateInput(attrs={'type': 'date'}),
                           help_text='The entered name and date will be displayed temporarily but publicly in the '
                                     'generated "Hello World" message. It will not be stored.')
