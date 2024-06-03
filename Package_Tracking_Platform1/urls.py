from django.urls import path
from .views import landing_page, signup, login_view, dashboard, profile, logout_view

urlpatterns = [
    path('', landing_page, name='landing_page'),  # Use landing_page from local views
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_view, name='logout'),
]

