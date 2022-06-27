"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inner import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('blog/post/', views.blog,name="post"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.signin, name="login"),
    path('logout/', views.logouts, name="logout"),
    path('settings', views.settings, name="settings"),
    path('userblogs/', views.userblogs, name="userblogs"),
    path('delete/<int:pk>/', views.delete_post, name="delete"),
    path('editblogs/<int:id>/',views.edit_blogs, name="editblogs"),
    path('readmore/<int:id>/', views.readmore, name="readmore"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
