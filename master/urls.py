from django.contrib import admin
from django.urls import path
from accounts import views as accountsViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accountsViews.homepage),
    path('login/', accountsViews.login),
    path('register/', accountsViews.register)
]
