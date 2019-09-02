from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import PasswordChangeForm

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
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')
        old_password = self.cleaned_data.get('old_password')

        if user.check_password(old_password):
            if new_password1 == old_password:
                raise forms.ValidationError("New password must be different than the old password")

        if new_password1 != new_password2:
            raise forms.ValidationError("Password confirmation did not match")

        return self.cleaned_data
