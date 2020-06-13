from django.contrib import admin
from .models import PersonalInfo
# Register your models here.


class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'phonenumber')


admin.site.register(PersonalInfo,PersonalInfoAdmin)

