from django.shortcuts import render
from .forms import MathExpressionForm


def home_index(request):
    form = MathExpressionForm(request.POST or None)

    return render(request,
                  'lab1/home_index.html', {'form': form})
