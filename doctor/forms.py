from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Doctor, Enterprise, Profile
from django.db import transaction



class SignupForm(UserCreationForm):
    name = forms.CharField(required=False, label='이름')
    birth = forms.CharField(required=False, label='생년월일')
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('name', 'birth')
        widgets = {
            'username': forms.EmailInput(attrs={
                'placeholder': 'Email',
            }),
        }


    def save(self, commit=True):
        with transaction.atomic():
            user = super(SignupForm, self).save()
            user.refresh_from_db()
            user.profile.name = self.cleaned_data.get('name')
            user.profile.birth = self.cleaned_data.get('birth')
            user = super().save(False)
            user.email = user.username
            user = super().save()
            return user

class EditProfileForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ['name', 'birth', 'wallet_address', 'image']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.EmailInput(attrs={
                'placeholder': 'Email',
            })
        }



class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = (
            'name',
            'medical_name',
            'address',
            'phone_number',
            'license_number',
            'certification'
        )

class EnterpriseForm(forms.ModelForm):
    class Meta:
        model = Enterprise
        fields = ('enterprise_name', 'enterprise_category')

