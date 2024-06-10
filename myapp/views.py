from django.shortcuts import render
from .models import Case

def index(request):
    cases = Case.objects.all()
    return render(request, 'myapp/index.html', {'cases': cases})
