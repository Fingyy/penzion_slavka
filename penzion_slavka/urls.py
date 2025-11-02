"""
URL configuration for penzion_slavka project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from penzion.views import (HomeView, OkoliView, KontaktView, CenikView, PokojeView, FotogalerieView, RoomTypeCreateView,
    OrderCreateView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('okoli/', OkoliView.as_view(), name='okoli'),
    path('kontakt', KontaktView.as_view(), name='kontakt'),
    path('cenik', CenikView.as_view(), name='cenik'),
    path('pokoje', PokojeView.as_view(), name='pokoje'),
    path('fotogalerie', FotogalerieView.as_view(), name='fotogalerie'),
    # path('rezervace', RoomTypeCreateView.as_view(), name='rezervace'),
    path('rezervace', OrderCreateView.as_view(), name='rezervace'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
