from django.shortcuts import render

from .utils import Function, OrdinaryLeastSquares, TaylorMethod
from .forms import MathExpressionForm


def home_index(request):
    form = MathExpressionForm(request.POST or None)
    firstf = second_data = third_data = None
    if form.is_valid():
        data = form.cleaned_data
        firstf = Function(data['expression'], data['start'], data['end'], data['step'])
        secondf = OrdinaryLeastSquares(firstf)
        second_data = Function(secondf.get_expression, data['start'], data['end'], data['step'])
        thirdf = TaylorMethod(data['expression'], firstf.middle_point)
        third_data = Function(thirdf.get_expression, data['start'], data['end'], data['step'])
    return render(request,
                  'lab1/home_index.html', {'form': form,
                                           'first': firstf,
                                           'second': second_data,
                                           'third': third_data})
