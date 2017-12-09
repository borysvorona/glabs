from django.shortcuts import render

from .utils import Function, OrdinaryLeastSquares
from .forms import MathExpressionForm


def home_index(request):
    form = MathExpressionForm(request.POST or None)
    firstf = secondf = thirdf = None
    if form.is_valid():
        data = form.cleaned_data
        firstf = Function(data['expression'], data['start'], data['end'], data['step'])
        print(firstf.get_result)
        secondf = OrdinaryLeastSquares(firstf).get_expression
        print(secondf)
    return render(request,
                  'lab1/home_index.html', {'form': form,
                                           'first': firstf.get_result,
                                           'second': secondf,
                                           'third': thirdf})
