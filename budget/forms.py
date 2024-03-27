from django import forms
from .models import Expense

class ExpenseForm(forms.Form):
    class Meta:
        model=Expense
        fields=['title','amount','category']
 