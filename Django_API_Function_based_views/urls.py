from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', views.students_list),
    path('students/', views.students_details),

]