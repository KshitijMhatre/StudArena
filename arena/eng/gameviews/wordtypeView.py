from django.shortcuts import render
from ..games import wordtype
from django.http import HttpResponse

def index(request):
    return render(request,'eng/wordtype.html',wordtype.challenge())