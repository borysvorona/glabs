from django.shortcuts import render

from .utils import Function, OrdinaryLeastSquares, TaylorMethod
from .forms import MathExpressionForm


def home_index(request):
    form = MathExpressionForm(request.POST or None)
    firstf = secondf = thirdf = None
    if form.is_valid():
        data = form.cleaned_data
        firstf = Function(data['expression'], data['start'], data['end'], data['step'])
        print(firstf.get_result)
        secondf = OrdinaryLeastSquares(firstf)
        print(secondf.get_expression)
        thirdf = TaylorMethod(data['expression'], firstf.middle_point)
        print(thirdf.get_expression)
    return render(request,
                  'lab1/home_index.html', {'form': form,
                                           'first': firstf.get_result,
                                           'second': secondf.get_expression,
                                           'third': thirdf.get_expression})
