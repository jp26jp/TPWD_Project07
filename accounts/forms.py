from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.password_validation import validate_password

from .models import Account


class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'dob', 'email', 'email_confirmation', 'bio', 'avatar']

    def clean(self, *args, **kwargs):
        cleaned_data = super(EditProfileModelForm, self).clean()
        email = self.cleaned_data.get('email')
        email_confirmation = self.cleaned_data.get('email_confirmation')
        if email and email_confirmation and email != email_confirmation:
            raise forms.ValidationError("Emails do not match")
        return cleaned_data


class PasswordChangeFormExt(PasswordChangeForm):
    """Form for changing user's password."""

    def clean(self):
        user = self.user
        new_password = self.cleaned_data.get('new_password1')
        old_password = self.cleaned_data.get('old_password')

        validate_password(new_password, user)

        if user.check_password(old_password):
            if new_password == old_password:
                raise forms.ValidationError("New password must be different than the old password")

        if user.first_name.lower() in new_password.lower() or user.last_name.lower() in new_password.lower():
            raise forms.ValidationError("You cannot use personal information in your password")

        return self.cleaned_data
