from django.shortcuts import render

# Create your views here.

data={
    'games' : [
        {
            'name' :  'Word type',
            'url'  :  '/english/wordtype'
        },
    ]
}

def index(request):
    return render(request,'eng/index.html',{'games' : data})
