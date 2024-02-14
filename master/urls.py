from django.contrib import admin
from django.urls import path
from accounts import views as accountsViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accountsViews.homepage, name='homepage'),
    path('login/', accountsViews.loginpage, name='loginpage'),
    path('register/', accountsViews.registerpage, name='registerpage'),
    path('dashboard/', accountsViews.dashboard, name='dashboard'),
]
