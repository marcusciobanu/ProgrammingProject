from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('home/', views.home, name='home'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout')
]
