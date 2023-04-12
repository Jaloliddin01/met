from django import forms

class ExpenseForm(forms.Form):
    user = forms.CharField(max_length=20)
    amount = forms.FloatField()
    description = forms.CharField(max_length=100)
    category = forms.CharField(max_length=20)
