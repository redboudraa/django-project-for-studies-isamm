from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterForm(forms.Form):
    username = forms.CharField(label='Username', 
                widget=forms.Textarea(
                        attrs={'placeholder': "", 
                            "class": "form-control","rows":"2"}
                    ))
    email = forms.EmailField(label='Email', 
                widget=forms.Textarea(
                        attrs={'placeholder': "", 
                            "class": "form-control","rows":"2"}
                    ))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                            "class": "form-control","rows":"2"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
                            "class": "form-control","rows":"2"}))


    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Password must match")
        return password2

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__icontains=username).exists():
            raise forms.ValidationError("This username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__icontains=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email