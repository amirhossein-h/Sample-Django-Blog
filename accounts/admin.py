from django.contrib import admin
from .models import ContactMe

@admin.register(ContactMe)
class ContactMeAdmin(admin.ModelAdmin):
    list_display = ["user", "email", "datetime_created", "short_text"]

    def short_text(self, obj):
        return obj.text[:30]