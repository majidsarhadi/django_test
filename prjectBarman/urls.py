from django.urls import path
from django.views.generic import DeleteView

from . import views
from .views import CreateStudent, ShowStudentList, UpdateStudent, DeleteStudent

urlpatterns = [
    path("register/",CreateStudent.as_view(),name="create"),
    path("Show/",ShowStudentList.as_view(),name="show"),
    path("update/<pk>",UpdateStudent.as_view(),name="update"),
    path('<pk>/delete/',DeleteStudent.as_view(),name="delete"),
]