from django.contrib import admin

# Locals Forms
from .forms import AccountCreationForm, AccountEditForm

# Locals Models
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    """
        Account Admin
    """
    list_display = ("id", "login", "email", "status")
    search_fields = ["login", "email"]
    form = AccountEditForm
    add_form = AccountCreationForm

    def get_form(self, request, obj=None, **kwargs):
        """
        Use special form during user creation
        """
        defaults = {}
        if obj is None:
            defaults["form"] = self.add_form
        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)


admin.site.register(Account, AccountAdmin)
