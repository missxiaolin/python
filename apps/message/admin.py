from django.contrib import admin

# Register your models here.

from .models import UserProfile
from .models import EmailVerifyRecord


class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile, UserProfileAdmin)

class EmailVerifyRecordAdmin(admin.ModelAdmin):
    pass

admin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
