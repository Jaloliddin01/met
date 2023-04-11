from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .models import User

class UserRegistrationView(View):
    def post(self, request: HttpRequest) -> JsonResponse:
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return JsonResponse({'status': 'user created successfully'})
        return JsonResponse({'status': 'failed'})

class UserLoginView(View):
    def post(self, request: HttpRequest) -> JsonResponse:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse({'status': 'logged in successfully'})
        return JsonResponse({'status': 'login failed'})

class UserLogoutView(View):
    def post(self, request: HttpRequest) -> JsonResponse:
        logout(request)
        return JsonResponse({'status': 'logged out successfully'})
