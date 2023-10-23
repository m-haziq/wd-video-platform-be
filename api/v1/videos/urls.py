from django.urls import path

from . import views


urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('rate-video/<int:video_id>/', views.RatingView.as_view(), name='rate_update'),
    path('remove-video/<int:video_id>/', views.RemoveVideoView.as_view(), name='remove_video'),
]
