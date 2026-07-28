from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:

        model = Employee

        fields = [
            'name',
            'email',
            'phone',
            'gender',
            'department',
            'designation',
            'salary',
            'address',
            'photo',
        ]


        widgets = {

            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter employee name'
                }
            ),


            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter email'
                }
            ),


            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter phone number'
                }
            ),


            'gender': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),


            'department': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter department'
                }
            ),


            'designation': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter designation'
                }
            ),


            'salary': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter salary'
                }
            ),


            'address': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'placeholder': 'Enter address'
                }
            ),


            'photo': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control'
                }
            ),

        }