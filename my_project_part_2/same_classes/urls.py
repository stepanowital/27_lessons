from same_classes import views
from django.urls import path

# TODO здесь необходимо настроить urls
urlpatterns = [
   path("feedback/", views.FeedbackView.as_view(), name="feedback"),
   path("feedback/<int:pk>/", views.FeedbackEntityView.as_view(), name="feedback_entity"),
]
