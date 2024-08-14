from django import forms
from .models import TitanicPassenger

class TitanicPassengerForm(forms.ModelForm):
    class Meta:
        model = TitanicPassenger
        fields = [
            'passenger_id', 'survived', 'pclass', 'name', 'sex', 
            'age', 'sibsp', 'parch', 'ticket', 'fare', 'cabin', 'embarked'
        ]
        widgets = {
            'sex': forms.Select(choices=[('male', 'Male'), ('female', 'Female')]),
            'embarked': forms.Select(choices=[('C', 'Cherbourg'), ('Q', 'Queenstown'), ('S', 'Southampton')]),
            'survived': forms.Select(choices=[(0, 'No'), (1, 'Yes')]),
            'pclass': forms.Select(choices=[(1, 'First'), (2, 'Second'), (3, 'Third')])
        }


class UploadFileForm(forms.Form):
    file = forms.FileField()
