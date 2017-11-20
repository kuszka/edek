from django.shortcuts import render
from pomiar import Pomiar
# Create your views here.


def index(request):
    values_from_acceler = Pomiar()
    return render(request,'sensors/index.html',values_from_acceler)
