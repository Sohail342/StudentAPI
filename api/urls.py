from django.urls import path
from . import views

urlpatterns = [
    path('api/list/', views.StudentsList.as_view(), name="student_list"),
]
