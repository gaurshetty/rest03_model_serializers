from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['no', 'name', 'age', 'salary', 'address']


admin.site.register(Employee, EmployeeAdmin)
