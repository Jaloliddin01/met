import django_filters

from .models import Expense

class ExpenseFilter(django_filters.FilterSet):
    class Meta:
        model = Expense
        fields = {
            'amount': ['lt', 'gt'],
            'description': ['icontains'],
            'category': ['exact'],
            'user': ['exact'],
        }