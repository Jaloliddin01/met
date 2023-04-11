from django.urls import path
from .views import UserRegistrationView, ExpenseView, HomeView, CategoryView, AboutView

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("registration/", UserRegistrationView.as_view(), name='registration'),
    path("expenses/", ExpenseView.as_view(), name='expenses'),
    path("categories/", CategoryView.as_view(), name='category'),
    path("about/", AboutView.as_view(), name='about'),
]