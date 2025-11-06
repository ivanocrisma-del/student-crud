from django.contrib import admin
from django.urls import path, include
from students.views import student_dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('student/', student_dashboard, name='student_dashboard'),
    path('', student_dashboard, name='home'),
]
