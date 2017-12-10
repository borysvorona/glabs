import decimal
from django.forms import ModelForm, forms
from lab1.models import MathExpression


class MathExpressionForm(ModelForm):
    class Meta:
        model = MathExpression
        fields = ['expression', 'start', 'end',  'step']
        # exclude = ['step']

    def clean(self):
        cleaned_data = self.cleaned_data
        start = cleaned_data.get('start')
        end = cleaned_data.get('end')
        step = cleaned_data.get('step')
        if start >= end:
            raise forms.ValidationError('Wrong interval, enter another one')
        if step is None:
            step = MathExpression._meta.get_field('step').get_default()
            cleaned_data['step'] = decimal.Decimal(step)
        if step and step >= (end - start):
            raise forms.ValidationError('Wrong step, enter another one')
        return cleaned_data
