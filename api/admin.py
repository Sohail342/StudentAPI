from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Student
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm

@admin.register(Student)
class StudentAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm
    list_display = ('student_name', 'nationality', 'city', 'gender')
    search_fields = ('student_name', 'nationality', 'city', 'gender')
    list_filter = ('gender', 'nationality')