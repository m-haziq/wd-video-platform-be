from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', admin.site.urls),

    path('api/v1/account/', include('api.v1.accounts.urls')),
    path('api/v1/video/', include('api.v1.videos.urls')),
]
