from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Video, Ratings, Dashboard
from .serializers import RatingUpdateSerializer, DashboardSerializer


class DashboardView(APIView):

    def get(self, request):
        user = request.user

        try:
            dashboard, created = Dashboard.objects.get_or_create(user=user)
            if created:
                all_videos = Video.objects.all()
                dashboard.videos.set(all_videos)
                dashboard.save()

            serializer = DashboardSerializer(dashboard)
            return Response(serializer.data)

        except Dashboard.DoesNotExist:
            return Response({"error": "User dashboard not found"}, status=status.HTTP_404_NOT_FOUND)


class RatingView(APIView):

    def put(self, request, video_id):
        try:
            video = Video.objects.get(pk=video_id)
        except Video.DoesNotExist:
            return Response({"error": "Video not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = RatingUpdateSerializer(data=request.data)

        if serializer.is_valid():
            rating_value = serializer.validated_data['rating']
            user = request.user

            try:
                if Ratings.objects.get(video=video, user=user).indexes():
                    return Response(
                        {"message": "You have already rated this video"},
                        status=status.HTTP_400_BAD_REQUEST
                    )

            except Ratings.DoesNotExist:
                Ratings.objects.create(video=video, user=user, rating=rating_value)
            return Response({"message": "Rating updated successfully"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RemoveVideoView(APIView):

    def delete(self, request, video_id):
        user = request.user

        try:
            video = Video.objects.get(id=video_id)
        except Video.DoesNotExist:
            return Response({"error": "Video not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            dashboard = Dashboard.objects.get(user=user)

            if video in dashboard.videos.all():
                dashboard.videos.remove(video)
                return Response({"message": "Video removed from dashboard"}, status=status.HTTP_200_OK)

            else:
                return Response({"error": "Video not found in the dashboard"}, status=status.HTTP_404_NOT_FOUND)

        except Dashboard.DoesNotExist:
            return Response({"error": "User dashboard not found"}, status=status.HTTP_404_NOT_FOUND)
