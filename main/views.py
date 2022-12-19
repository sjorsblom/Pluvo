from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.forms import ScoreSelectionForm, GradeForm
from main.models import Score, User
import datetime
from django.contrib.auth.decorators import user_passes_test

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

    return render(request, 'main/scores.html', {
        'form': form,
        'scores': scores
    })


@login_required(login_url='/login')
@user_passes_test(lambda u: u.is_superuser)
def teacher_view(request):
    """ Teacher page """
    form = GradeForm()
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            user = User.objects.get(pk=form.cleaned_data['user'])
            score = Score(user=user, score=form.cleaned_data['grade'], date=datetime.datetime.now())
            score.save()
            print(score)

    return render(request, 'main/teacher.html', {
        'form': form
    })


    

