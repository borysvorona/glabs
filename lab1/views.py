from django.shortcuts import render
from .utils import *

from .forms import MathExpressionForm


def home_index(request):
    form = MathExpressionForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        first = get_chart_points(data['expression'], data['start'], data['end'], data['step'])
        print(first)
    return render(request,
                  'lab1/home_index.html', {'form': form})


def get_chart_points(expr, start, end, step):
    #   1+ctg(x/2)-(1-2*cos(x/2)**2)+sin(x)**2
    x = start
    result = []
    while x < end:
        try:
            result.append([float(x), eval(expr)])
        except ZeroDivisionError:
            print('Gap at point %s. Solution does not exist:' % x)
            result.append([float(x), None])
        x += step
    return result
