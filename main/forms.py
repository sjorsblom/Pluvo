from django.core.exceptions import ValidationError
from django.forms import Form, SelectDateWidget
from django.forms.fields import ChoiceField, DateField
from main.models import User
import datetime

class ScoreSelectionForm(Form):
    start = DateField(label="Grades from:", initial=lambda: datetime.date.today() - datetime.timedelta(days=7), required=True, widget=SelectDateWidget)
    end = DateField(label="Grades until:", initial=datetime.date.today, required=True, widget=SelectDateWidget)
    user = ChoiceField(label="User:", choices=[], required=True)

    def __init__(self, *args, **kwargs):
        super(ScoreSelectionForm, self).__init__(*args, **kwargs)
        self.fields['user'].choices = [(x.pk, x.username) for x in User.objects.all()]

    def clean(self):
        cleaned_data = super(ScoreSelectionForm, self).clean()
        if cleaned_data['end'] < cleaned_data['start']:
            raise ValidationError("End date should come after the start date!!")
        return cleaned_data