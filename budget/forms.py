from django import forms
from .models import Expense
from django.forms import ModelForm

class ExpenseForm(ModelForm):
   class Meta:
      model=Expense
      fields=['title','amount','category']
#    title=forms.CharField()
#    amount=forms.IntegerField()
#    category=forms.CharField()
 