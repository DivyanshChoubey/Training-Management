__all__ = [
    "TrainerCreateSerializer",
    "ModuleCreateSerializer",
    "ResourceCreateSerializer",
    "ResourceSerializer",
    "ModuleSerializer",
    "TrainerSerializer",
]

from service.serializers.trainer_create_serializer import TrainerCreateSerializer
from service.serializers.module_create_serializer import ModuleCreateSerializer
from service.serializers.resource_create_serializer import ResourceCreateSerializer
from service.serializers.trainer_detail_serializer import ResourceSerializer, ModuleSerializer, TrainerSerializer
