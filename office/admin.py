from django.contrib import admin
from django.utils.safestring import mark_safe

from office.models import Staff, Department


class StaffAdmin(admin.ModelAdmin):
    list_display = ('lastname', 'firstname', 'patronymic', 'department', 'dateOfBirth', 'startDateWork', 'get_photo')

    def get_photo(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" width="75">')


admin.site.register(Staff, StaffAdmin)
admin.site.register(Department)
