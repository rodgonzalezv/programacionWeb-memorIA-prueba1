from django.shortcuts import render
from .models import Familiar

# Create your views here.
def home(request):
    familia = Familiar.objects.get(id=1)
    context = {"user": request.user, "familia": familia}
    return render(request, "memoria/index.html", context)
