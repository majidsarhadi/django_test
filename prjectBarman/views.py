from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from prjectBarman.models import Student


# Create your views here.
class CreateStudent(CreateView):
    model = Student
    fields = ["full_name","email","address","nation_id","phone","user_name","password"]
    success_url = reverse_lazy("show")
    template_name = "register_student.html"

class ShowStudentList(ListView):
    model = Student
    template_name = "show_student.html"
    context_object_name = "students"
    def get_queryset(self,*args, **kwargs):
        qs=super(ShowStudentList,self).get_queryset(*args, **kwargs)
        return qs

class UpdateStudent(UpdateView):
  model = Student
  fields = ["full_name", "email", "address", "nation_id", "phone", "user_name", "password"]
  success_url = reverse_lazy("show")
  template_name = "update_student.html"

class DeleteStudent(DeleteView):
   model = Student
   success_url = reverse_lazy("show")
   template_name = "delete_student.html"


def show(request):
    return render(request,"show_template.html")