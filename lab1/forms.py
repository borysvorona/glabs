from django.forms import ModelForm
from lab1.models import MathExpression


class MathExpressionForm(ModelForm):
    class Meta:
        model = MathExpression
        fields = ['start', 'end', 'expression']
