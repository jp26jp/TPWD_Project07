from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

class UniquenessValidator:
    def validate(self, password, user=None):
        if user.check_password(old_password):
            if new_password == old_password:
                raise forms.ValidationError("New password must be different than the old password")
