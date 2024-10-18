from django import forms

class AmountForm(forms.Form):
    includeTerms = forms.CharField(label='Enter your Investment Total($)', required=False,widget=forms.NumberInput(attrs={
            'placeholder': 'Enter amount',
            'class': 'form-control', #type="text" class="form-control" id="includeTerms" placeholder="Comma-separated terms"
            'id': 'includeTerms'
        }))
    # excludeTerms = forms.CharField(label='Exclude Terms', required=False, widget=forms.TextInput(attrs={
    #         'placeholder': 'Comma-separated terms',
    #         'class': 'form-control', #type="text" class="form-control" id="excludeTerms" placeholder="Comma-separated terms"
    #         'id':'excludeTerms'
    #     }))




class DesiredAmountForm(forms.Form):
    includeTerms = forms.CharField(label='Enter your Desired Amount($)', required=False,widget=forms.NumberInput(attrs={
            'placeholder': 'Enter amount',
            'class': 'form-control', #type="text" class="form-control" id="includeTerms" placeholder="Comma-separated terms"
            'id': 'includeTerms'
        }))