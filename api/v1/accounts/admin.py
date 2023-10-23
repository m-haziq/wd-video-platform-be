from django.contrib import admin
from api.v1.accounts.models import CustomUser
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model


User = get_user_model()

# Register your models here.
admin.site.register(CustomUser)
admin.site.unregister(Group)
admin.site.unregister(User)

