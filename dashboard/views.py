from django.shortcuts import render, redirect
from .forms import DataForm
from .models import Data
from django.http.response import JsonResponse


 


from rest_framework.decorators import api_view

# Create your views here.

#@api_view(['POST',])
def index(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-predictions')
    else:
        form = DataForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/index.html', context)


def predictions(request):
    spam_detection = Data.objects.all()
    context = {
        'spam_detection': spam_detection
    }
    return render(request, 'dashboard/predictions.html', context)

