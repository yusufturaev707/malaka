from django.contrib.auth import get_user_model
from django import forms
from django.forms import Select, TextInput, NumberInput, Textarea, FileInput, CheckboxInput
from django.contrib.auth.forms import UserCreationForm
from bootstrap_datepicker_plus.widgets import DatePickerInput

from refresher_course.models import Certificate, Course, Nation, CourseComplete

User = get_user_model()


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']


class CreateCertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['first_name', 'last_name', 'middle_name', 'jshshr', 'invoice', 'nationality', 'course', 'start_date',
                  'end_date', 'month', 'year', 'cer_nomer', 'status', 'registered_day', 'registered_number']

        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter...",
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter...",
            }),
            'middle_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter...",
            }),
            'jshshr': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter...",

            }),
            'invoice': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter...",

            }),
            'nationality': Select(attrs={
                'class': 'form-control',
                'data-live-search': "true",
                'data - style': "btn-white",
            }),
            'course': Select(attrs={
                'class': 'form-control',
                'data-live-search': "true",
                'data - style': "btn-white",
            }),
            'start_date': NumberInput(attrs={
                'class': 'form-control',
            }),
            'end_date': NumberInput(attrs={
                'class': 'form-control',
            }),
            'month': Select(attrs={
                'class': 'form-control',
                'data-live-search': "true",
                'data - style': "btn-white",
                'data - parsley - required': "true",
            }),
            'year': Select(attrs={
                'class': 'form-control',
                'data-live-search': "true",
                'data - style': "btn-white",
                'data - parsley - required': "true",
            }),
            'cer_nomer': NumberInput(attrs={
                'class': 'form-control',
            }),
            'registered_number': NumberInput(attrs={
                'class': 'form-control',
                'name': 'registered_number',
            }),
            'registered_day': TextInput(attrs={
                'class': 'form-control',
                'name': 'registered_day',
            }),

        }


class CourseCompleteForm(forms.ModelForm):
    class Meta:
        model = CourseComplete
        fields = ['course', 'start_date', 'end_date', 'month', 'year', 'file', 'begin_cer_nomer', 'nationality',
                  'certificate_turi']

        widgets = {
            'course': Select(attrs={
                'class': 'form-control selectpicker',
                'data - size': "10",
                'data-live-search': "true",
                'data - style': "btn-white",
                'data - parsley - required': "true",
            }),
            'file': FileInput(attrs={
                'id': 'id_file',
                'name': 'file',
                'class': 'form-control',
                'data - parsley - required': "true",
                'accept': ".xlsx, .xls, .csv"
            }),
            'start_date': TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': "Enter...",
                'data - parsley - required': "true",
            }),
            'end_date': TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': "Enter...",
                'data - parsley - required': "true",
            }),
            'month': Select(attrs={
                'class': 'form-control selectpicker',
                'data - size': "10",
                'data-live-search': "true",
                'data - style': "btn-white",
                'data - parsley - required': "true",
            }),
            'nationality': Select(attrs={
                'class': 'form-control selectpicker',
                'data - size': "10",
                'data-live-search': "true",
                'data - style': "btn-white",
                'data - parsley - required': "true",
            }),
            'year': Select(attrs={
                'class': 'form-control selectpicker',
                'data - size': "10",
                'data-live-search': "true",
                'data - style': "btn-white",
                'data - parsley - required': "true",
            }),
            'certificate_turi': Select(attrs={
                'class': 'form-control selectpicker',
                'data - size': "10",
                'data-live-search': "true",
                'data - style': "btn-white",
                'data - parsley - required': "true",
            }),
        }


class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'language', 'hour_course', 'is_visible_hour', 'status']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
            }),
            'hour_course': NumberInput(attrs={
                'class': 'form-control',
            }),
            'language': Textarea(attrs={
                'class': 'form-control',
            }),
        }


class CreateNationForm(forms.ModelForm):
    class Meta:
        model = Nation
        fields = ['name', 'key', 'status']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter...",
            }),
            'key': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter...",
            }),
        }
