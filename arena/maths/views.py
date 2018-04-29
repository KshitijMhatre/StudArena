from django.shortcuts import render
from .games import funmat
from django.http import HttpResponse
import random

# Create your views here.
questions={
    1:"Biggest number formed with digits of",
    2:"Biggest Odd number formed with digits of",    
    3:"Biggest Even number formed with digits of",
    4:"Smallest number formed with digits of",
    5:"Smallest Odd number formed with digits of",
    6:"Smallest Even number formed with digits of",
}

def index(request):
    q=random.randint(1000,9999)
    qnum = random.randint(1,6)
    return render(request, 'maths/index.html' ,{'num':q,
                                                'qnum':qnum,
                                                'question':questions[qnum],
                                                'digs':funmat.digits(q),

                            })

def check(resquest):
    resp = int(resquest.POST.get("num"))
    qnum = int(resquest.POST.get("qnum"))
    q=int(resquest.POST.get("q"))
    funs={
        1:funmat.big,
        2:funmat.bigo,
        3:funmat.bige,
        4:funmat.small,
        5:funmat.smallo,
        6:funmat.smalle,
    }
    ans= funs[qnum](q)
    if funmat.ask_n_check(ans,resp,"ans num is"):
        return HttpResponse("Correct")
    else:
        if ans==-1:
            ans= "not possible"
        return HttpResponse("InCorrect<br> right ans is "+str(ans))
