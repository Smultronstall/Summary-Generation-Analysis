from django.shortcuts import render
from django.http import JsonResponse
from .models import Text
from django.utils import timezone
# Create your views here.


def index(request):
    msg = {}
    msg["status"] = 0
    return render(request, './index.html', context=msg)


def summarize(request):
    msg = {}
    msg["status"] = 0
    if request.method == 'POST':
        dic = request.POST
        original_text = dic["original-text"]
        #CODE HERE TO GENERATE THE SUMMARY
        msg["input"] = original_text
        msg["output"] = original_text
        msg["status"] = 1
        new_text = Text(content=original_text)
        new_text.save()
    return JsonResponse(msg)
