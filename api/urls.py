from django.urls import path
from . import views

urlpatterns = [
    path('api/list/', views.StudentsListView.as_view(), name="student_list"), 
    path('api/create/', views.StudentCreateView.as_view(), name="student_create"), 
    path('api/delete/<int:pk>/', views.StudentDeleteView.as_view(), name="student_delete"),
]
