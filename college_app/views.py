from django.http import HttpResponse
from django.views.generic import View, TemplateView, DetailView, ListView, CreateView, UpdateView, DeleteView
from college_app import models
from django.core.urlresolvers import reverse_lazy

# from college_app import models

# Create your views here.

# class IndexView(View):
#     def get(self, request):
#         return HttpResponse('hello world')

class IndexView(TemplateView):
    template_name = 'college_app/index.html'

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'college_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ("name", "principal")
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ("name", "principal")
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("college_app:list")
