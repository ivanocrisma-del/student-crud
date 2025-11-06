from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Student
from .forms import StudentForm


class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'

    def get_queryset(self):
        """Allow searching students by name."""
        query = self.request.GET.get('q')
        if query:
            return Student.objects.filter(Q(name__icontains=query))
        return Student.objects.all()

    def get_context_data(self, **kwargs):
        """Pass search query back to template."""
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('students:list')


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('students:list')


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('students:list')


def student_dashboard(request):
    """Display the student dashboard (not required if using list view)."""
    students = Student.objects.all()
    return render(request, 'students/dashboard.html', {'students': students})


def get_queryset(self):
    query = self.request.GET.get('q')  
    if query:
        return Student.objects.filter(Q(name__icontains=query))
    return Student.objects.all()

