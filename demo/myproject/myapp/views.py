from django.http import HttpResponse
from django.shortcuts import render
from .models import travel, team


def home(request):
    obj = travel.objects.all()
    result = team.objects.all()
    return render(request, "home.html", {'result': obj, 'res': result})


# def addition(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     result = x + y
#     result1 = x - y
#     result2 = x * y
#     result3 = x / y
#     return render(request, "result.html", {'result': result, 'res1': result1, 'res2': result2, 'res3': result3})
