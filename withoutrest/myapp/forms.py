from django import forms
from .models import Employee

class EmpForm(forms.ModelForm):
    def clean_sal(self):#clean salary details
        inputsal=self.cleaned_data['esal']
        if inputsal<5000:
            raise forms.ValidationError('the min salary should be 5000')
        return inputsal
    class Meta:
        model=Employee
        fields='__all__'