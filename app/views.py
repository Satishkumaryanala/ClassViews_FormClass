from django.shortcuts import render
from django.views.generic import FormView,ListView
from django.http import HttpResponse
from django.db.models.functions import Length
# Create your views here.

from app.forms import *

class SchoolInsert_FV(FormView):
    form_class = SchoolForm
    template_name = 'SchoolInsert_FV.html'

    def form_valid(self,form):
        form.save()
        return HttpResponse('<center><h1 style="color: green;">Data inserted successfully</h1></center>')


class SchoolList(ListView):
    model = School
    queryset = School.objects.order_by(Length('Sprin').desc())
    template_name = 'SchoolList.html'
    context_object_name = 'QSSO'
    # ordering = ['Sprin']



