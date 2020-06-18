from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def welcome(request):
    return render(request, "website/welcome.html",
                  {"var_1": "This data was sent from views file.",
                   "link": "https://pluralsight.com"})

def date(request):
    return HttpResponse("The currtent time is: " + str(datetime.now()))

def about(request):
    return HttpResponse("<p>Name: Aga Khan</p>"
                        "<p>Address: 99 Central Road</p>"
                        "<p>Cell: 01521226855</p>")