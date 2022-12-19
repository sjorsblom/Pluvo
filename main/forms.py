from django.core.exceptions import ValidationError
from django.forms import Form, DateInput, PasswordInput, TextInput, CharField, Select, FloatField, NumberInput
from django.forms.fields import ChoiceField, DateField
from main.models import User
import datetime
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class ScoreSelectionForm(Form):
    def __init__(self, *args, **kwargs):
        super(ScoreSelectionForm, self).__init__(*args, **kwargs)
        self.fields['user'].choices = [(x.pk, x.username) for x in User.objects.all()]

    start = DateField(label="", initial=lambda: datetime.date.today() - datetime.timedelta(days=7), required=True, widget=DateInput(
        attrs={
            'class': 'border-transparent',
            'type': 'date'
        }
    ))
    end = DateField(label="", initial=datetime.date.today, required=True, widget=DateInput(
        attrs={
            'class': 'border-transparent',
            'type': 'date'
        }))
    user = ChoiceField(label="User:", choices=[], required=True, widget=Select(
        attrs={
            'class': 'w-36 rounded-md border-gray-300 shadow-sm focus:border-pluvo_green focus:ring-pluvo_green sm:text-sm',
            'type': 'date'
        }
    ))

    def clean(self):
        cleaned_data = super(ScoreSelectionForm, self).clean()
        if cleaned_data['end'] < cleaned_data['start']:
            raise ValidationError("End date should come after the start date!!")
        return cleaned_data




class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(label='', widget=TextInput(
        attrs={
            'class': 'relative block w-full appearance-none rounded-none rounded-t-md border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-pluvo_green focus:outline-none focus:ring-pluvo_green sm:text-sm',
            'placeholder': 'Username'
        }))
    password = CharField(label='', widget=PasswordInput(
        attrs={
            'class': 'relative block w-full appearance-none rounded-none rounded-b-md border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-pluvo_green focus:outline-none focus:ring-pluvo_green sm:text-sm',
            'placeholder': 'Password'
        }
))


class GradeForm(Form):    
    def __init__(self, *args, **kwargs):
        super(GradeForm, self).__init__(*args, **kwargs)
        self.fields['user'].choices = [(x.pk, x.username) for x in User.objects.all()]

    user = ChoiceField(label="User:", choices=[], required=True, widget=Select(
        attrs={
            'class': 'block w-full rounded-md border-gray-300 shadow-sm focus:border-pluvo_green focus:ring-pluvo_green sm:text-sm',
            'type': 'date'
        }
    ))

    grade = FloatField(label='', min_value=1, max_value=10, step_size=0.01, widget=NumberInput(
        attrs={
            'class': 'relative block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-pluvo_green focus:outline-none focus:ring-pluvo_green sm:text-sm',
            'placeholder': 'Grade'
        }
    ))
