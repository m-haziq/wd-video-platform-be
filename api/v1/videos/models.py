from enum import Enum

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Video(models.Model):
    url = models.URLField(max_length=500)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='videos')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class RatingValue(Enum):
    ZERO = 0.0
    HALF = 0.5
    ONE = 1.0
    ONE_AND_A_HALF = 1.5
    TWO = 2.0
    TWO_AND_A_HALF = 2.5
    THREE = 3.0
    THREE_AND_A_HALF = 3.5
    FOUR = 4.0
    FOUR_AND_A_HALF = 4.5
    FIVE = 5.0


class Ratings(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings', null=True, blank=True)
    rating = models.FloatField(
        choices=[(rating.value, str(rating.name)) for rating in RatingValue],
        default=RatingValue.ZERO.value
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.video.title} - {self.rating}'


class Dashboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    videos = models.ManyToManyField(Video, related_name='dashboards', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - dashboard'


@receiver(post_save, sender=Video)
def update_dashboards(sender, instance, created, **kwargs):
    if created:
        dashboards = Dashboard.objects.all()

        for dashboard in dashboards:
            dashboard.videos.add(instance)
