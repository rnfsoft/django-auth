from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class SurveyCreateForm(forms.Form):
#     title = forms.CharField(label='Title', required=True, max_length=200)
#     questions = forms.MultiValueField(
#         required=True,
#         label="Questions",
#         widget=forms.MultipleHiddenInput()
#     )

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=150)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

