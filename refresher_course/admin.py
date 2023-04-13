from django.contrib import admin
from .models import Certificate, Nation, Course, CourseComplete, Page
from import_export.admin import ImportExportActionModelAdmin


@admin.register(Course)
class CourseAdmin(ImportExportActionModelAdmin):
    list_display = ['id', 'name', 'language', 'status', 'created_at', "hour_course"]
    list_filter = ['name', 'status']
    search_fields = ['name']


@admin.register(Page)
class PageAdmin(ImportExportActionModelAdmin):
    list_display = ['id', 'name', 'value']


@admin.register(Nation)
class NationAdmin(ImportExportActionModelAdmin):
    list_display = ['id', 'name', 'key', 'status']
    list_filter = ['name', 'key', 'status']
    search_fields = ['name', 'key']


@admin.register(Certificate)
class CertificateAdmin(ImportExportActionModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'middle_name', 'passport', 'nationality', 'course', 'start_date',
                    'end_date', 'month', 'year', 'cer_nomer',
                    'qr_code', 'status']
    list_filter = ['month', 'course', 'status', 'nationality', 'year']
    search_fields = ['first_name', 'last_name', 'middle_name', 'passport', 'start_date', 'end_date', 'month',
                     'cer_nomer']


@admin.register(CourseComplete)
class CourseCompleteAdmin(ImportExportActionModelAdmin):
    list_display = ['id', 'begin_cer_nomer', 'nationality', 'course', 'start_date', 'end_date', 'month', 'year', 'file']
    list_filter = ['month', 'course', 'nationality', 'course', 'year']
    search_fields = ['month', 'course']
