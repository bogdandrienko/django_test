from django.urls import path
from . import views

urlpatterns = [
    path('', views.ret_html),

    path('txt/', views.ret_str),
    path('txt_file/', views.ret_txt_file),

    path('json/', views.ret_json),
    path('json_file/', views.ret_json_file),

    path('excel_file/', views.ret_excel_file),
]
