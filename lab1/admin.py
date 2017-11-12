from django.contrib import admin
from lab1.models import MathExpression


class MathExpressionAdmin(admin.ModelAdmin):
    pass


admin.site.register(MathExpression, MathExpressionAdmin)
