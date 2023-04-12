from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Expense
from .filters import ExpenseFilter

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class UserRegistrationView(View):
    def get(self, request):
        return render(request, 'registration.html', {'status': 'registered successfully'})

class ExpenseView(ListView):

    model = Expense
    template_name = 'expenses.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['filter'] = ExpenseFilter(self.request.GET, queryset=self.get_queryset())
        return context

class CategoryView(View):
    def get(self, request):
        return render(request, 'category.html')

class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')
    
