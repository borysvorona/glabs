from django.db import models


class MathExpression(models.Model):
    start = models.DecimalField(max_digits=6, decimal_places=4, default=0.0)
    end = models.DecimalField(max_digits=6, decimal_places=4, default=1.0)
    expression = models.CharField(max_length=124)
    step = models.DecimalField(max_digits=4, decimal_places=2, default=0.1)

    class Meta:
        db_table = 'math_expression'

    def __str__(self):
        return "<Expression id=%s: %s>" % (self.id, self.expression)

    @property
    def label(self):
        return self.expression
