from django.contrib import admin
from django.urls import path
from accounts import views as accountsViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accountsViews.homepage),
    path('login/', accountsViews.loginpage),
    path('register/', accountsViews.registerpage, name='registerpage')
]
