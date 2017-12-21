
from django.shortcuts import render

from .utils import Function, OrdinaryLeastSquares, TaylorMethod, CoefficientOfDetermination
from .forms import MathExpressionForm


def home_index(request):
    form = MathExpressionForm(request.POST or None)
    answer = firstf = second_data = third_data = None
    if form.is_valid():
        data = form.cleaned_data
        answer = 'It is impossible to approximate, because the function has a discontinuity on this interval'
        firstf = Function(data['expression'], data['start'], data['end'], data['step'])
        if not firstf.has_break:
            secondf = OrdinaryLeastSquares(firstf)
            second_data = Function(secondf.get_expression, data['start'], data['end'], data['step'])
            thirdf = TaylorMethod(data['expression'], firstf.middle_point)
            third_data = Function(thirdf.get_expression, data['start'], data['end'], data['step'])
            result = CoefficientOfDetermination(firstf.get_abscissa_only, data['expression'],
                                                secondf.get_expression, thirdf.get_expression)
            answer = 'Оценка соответствия МНК: R^2 = %s%%;\n' \
                     'Оценка соответствия Ряд Тейлора: R^2 = %s%%.' % result.get_result

    return render(request,
                  'lab1/home_index.html', {'form': form,
                                           'first': firstf,
                                           'second': second_data,
                                           'third': third_data,
                                           'answer': answer})
