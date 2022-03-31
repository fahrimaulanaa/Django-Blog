from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1> Blog Home </h1>")

def about(request):
    return HttpResponse("<h1> About Blog </h1>"
    "<p> Dadi tugasmu iki nggawo soro awakmu dewe </p>"
    "<p> Sebelum kenek mental awakmu pindah RPL ae kene </p>")