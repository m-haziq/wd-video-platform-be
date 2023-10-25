from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='admin/', permanent=False)),
    path('api/v1/account/', include('api.v1.accounts.urls')),
    path('api/v1/video/', include('api.v1.videos.urls')),
]
