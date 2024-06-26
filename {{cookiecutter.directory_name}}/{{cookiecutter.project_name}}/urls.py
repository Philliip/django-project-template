"""updater_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.static import serve

from apps.api import urls as api_urlpatterns
from apps.api.views import status


urlpatterns = []
urlpatterns += [
    path(r'api/v1/', include(api_urlpatterns)),

    # Status
    path("status", status.StatusManagement.as_view(), name='status'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, view=serve)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, view=serve)
