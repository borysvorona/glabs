from django.shortcuts import render


def home_index(request):
    return render(request,
                  'lab1/home_index.html')
