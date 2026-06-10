__all__ = [
    "TrainerCreateView",
    "ModuleCreateView",
    "ResourceCreateView",
    "TrainerListView",
    "TrainerDetailView",
]

from service.views.trainer_create_view import TrainerCreateView
from service.views.module_create_view import ModuleCreateView
from service.views.resource_create_view import ResourceCreateView
from service.views.trainer_get_view import TrainerListView, TrainerDetailView
