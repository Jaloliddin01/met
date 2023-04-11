from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .models import User

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class UserRegistrationView(View):
    def get(self, request):
        return render(request, 'registration.html', {'status': 'registered successfully'})

class ExpenseView(View):
    def get(self, request):
        return render(request, 'expenses.html')

class CategoryView(View):
    def get(self, request):
        return render(request, 'category.html')

class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')
    

# class UserLoginView(View):
#     def post(self, request: HttpRequest) -> JsonResponse:
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             return JsonResponse({'status': 'logged in successfully'})
#         return JsonResponse({'status': 'login failed'})

# class UserLogoutView(View):
#     def post(self, request: HttpRequest) -> JsonResponse:
#         logout(request)
#         return JsonResponse({'status': 'logged out successfully'})
