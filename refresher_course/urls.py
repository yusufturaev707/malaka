from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    # path('change_qrcode/', change_qrcode, name='change_qrcode'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),

    path('certificates/', certificates, name='certificates'),
    path('certificates/create', create_certificate, name='create_certificate'),
    path('certificates/view/<int:pk>', view_certificate, name='view_certificate'),
    path('certificates/edit/<int:pk>', edit_certificate, name='edit_certificate'),
    path('certificates/delete/<int:pk>', delete_certificate, name='delete_certificate'),

    path('courses/', courses, name='courses'),
    path('courses/create', create_course, name='create_course'),
    path('courses/edit/<int:pk>', edit_course, name='edit_course'),
    path('courses/delete/<int:pk>', delete_course, name='delete_course'),

    path('nations/', nations, name='nations'),
    path('nations/create', create_nation, name='create_nation'),
    path('nations/edit/<int:pk>', edit_nation, name='edit_nation'),
    path('nations/delete/<int:pk>', delete_nation, name='delete_nation'),

    path('cerform/', fill_form, name='cerform'),
    path('complete_course/', complete_course, name='complete_course'),
    path('a_print/<int:pk>', a_print, name='a_print'),
    path('a_printone/<int:pk>', a_print_one, name='a_print_one'),
    path('searching/', searching, name='searching'),

    path("complete_course/<int:page>", complete_course, name="terms-by-page"),
    path("statistics/", statistics, name="statistics"),
    path("mydtm/", mydtm, name="mydtm"),
]
