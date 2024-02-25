from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('home/', views.home, name='home'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('create/', views.create, name='create'),
    path('create/<int:exercise_id>/', views.delete_exercise, name='delete_exercise'),
]
