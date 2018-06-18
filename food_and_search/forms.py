from django import forms
class research_product_form(forms.Form):
    product = forms.CharField(
        label='',
        max_length=100
    )
