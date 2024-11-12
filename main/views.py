from django.shortcuts import render
from django.http import HttpResponse

def index(reauest):
    return HttpResponse("<h4>Хеллоу ВОРЛД!!!!</h4>")
