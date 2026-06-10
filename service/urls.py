from django.urls import path

from service.views import *

urlpatterns = [
    path("trainer/create", TrainerCreateView.as_view(), name="trainer-create"),
    path("module/create", ModuleCreateView.as_view(), name="module-create"),
    path("resource/create", ResourceCreateView.as_view(), name="resource-create"),
    path("trainer/list", TrainerListView.as_view(), name="trainer-list"),
    path("trainer/<int:pk>/", TrainerDetailView.as_view(), name="trainer-details"),
]
