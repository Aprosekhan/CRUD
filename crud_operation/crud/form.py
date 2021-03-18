from django import forms

from .models import Post

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Name','Email','Password']
        widgets ={
            'Name': forms.TextInput(attrs={'class':'form-control'}),
            'Email': forms.EmailInput(attrs={'class':'form-control'}),
            'Password': forms.PasswordInput(attrs={'class':'form-control'})
        }