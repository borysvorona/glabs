import decimal
from django.forms import ModelForm, forms
from lab1.models import MathExpression


class MathExpressionForm(ModelForm):
    class Meta:
        model = MathExpression
        fields = ['expression', 'start', 'end',  'step']

    def __init__(self, *args, **kwargs):
        super(MathExpressionForm, self).__init__(*args, **kwargs)
        self.fields['expression'].initial = '1+cot(x/2)-(1-2*cos(x/2)**2)+sin(x)**2'

    def clean(self):
        cleaned_data = self.cleaned_data
        start = cleaned_data.get('start')
        end = cleaned_data.get('end')
        step = cleaned_data.get('step')
        if start >= end:
            msg = forms.ValidationError('Wrong interval, enter another one')
            self.add_error('start', msg)
        if step is None:
            step = MathExpression._meta.get_field('step').get_default()
            cleaned_data['step'] = decimal.Decimal(step)
        if step and step >= (end - start):
            msg = forms.ValidationError('Wrong step, enter another one')
            self.add_error('step', msg)
        return cleaned_data
