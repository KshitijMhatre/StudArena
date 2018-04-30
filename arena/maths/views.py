from django.shortcuts import render
from django.http import HttpResponse

data={
    'games' : [
        {
        'name' :  'funmat',
        'url'  :  '/maths/funmat'
        },
    ]
}

def index(request):
    return render(request,'maths/index.html',{'games' : data})
