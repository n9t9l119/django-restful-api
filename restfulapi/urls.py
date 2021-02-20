"""restfulapi URL Configuration

The `urlpatterns` list routes URLs to views_services. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views_services
    1. Add an import:  from my_app import views_services
    2. Add a URL to urlpatterns:  path('', views_services.home, name='home')
Class-based views_services
    1. Add an import:  from other_app.views_services import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('api/V1/geonames/', include('geonames.urls')),
    path('admin/', admin.site.urls),
]
