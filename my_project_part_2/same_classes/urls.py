from same_classes import views
from django.urls import path

urlpatterns = [
   path("feedback/", views.FeedbackView.as_view(), name="feedback"),
   path("feedback/<int:pk>/", views.FeedbackEntityView.as_view(), name="feedback_entity"),
   path("destination/", views.DestinationView.as_view()),
   path("destination/<int:pk>/", views.DestinationEntityView.as_view()),
   path("gen-destination/", views.DestinationListView.as_view()),
   path("gen-destination/<int:pk>/", views.DestinationDetailView.as_view()),
]
