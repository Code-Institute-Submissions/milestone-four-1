from django import forms
from .models import Commission

TYPES = [
    ('statue', 'Statue'),
    ('large_portrait', 'Large Portrait')
]


class CommissionForm(forms.ModelForm):

    class Meta:
        model = Commission
        fields = ('name', 'description')

    type = forms.CharField(label='Commission Type', widget=forms.Select(choices=TYPES))
