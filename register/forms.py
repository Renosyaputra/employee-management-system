from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullname', 'mobile', 'emp_code', 'position', 'profil_picture', 'cv_file')
        labels = {
            'fullname':'Full Name',
            'emp_code':'Registration No.',
            'profil_picture': 'Profile Picture', 
            'cv_file': 'Resume'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False
        self.fields['profil_picture'].required = False
        self.fields['cv_file'].required = False
