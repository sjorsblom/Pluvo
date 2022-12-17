from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.forms import ScoreSelectionForm
from main.models import Score
import datetime

# Create your views here.
@login_required(login_url='/login')
def dashboard_view(request):
    """ Dashboard page """
    scores = []

    form = ScoreSelectionForm()
    if request.method == 'POST':
        form = ScoreSelectionForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start']
            end_date = form.cleaned_data['end'] + datetime.timedelta(days=1) # Add a day to include current day
            scores = Score.objects.filter(user=form.cleaned_data['user']).filter(date__gte=start_date).filter(date__lt=end_date)

    return render(request, 'main/dashboard.html', {
        'form': form,
        'scores': scores
    })