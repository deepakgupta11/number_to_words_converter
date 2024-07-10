from django import forms

class AmountForm(forms.Form):
    amount = forms.IntegerField(label='Enter amount', min_value=1, max_value=9999999999)
