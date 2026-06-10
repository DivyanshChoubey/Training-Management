from rest_framework import serializers

from service.models import Resource, Trainer, TrainingModule


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ["id", "name"]

class ModuleSerializer(serializers.ModelSerializer):
    resources = ResourceSerializer(many=True, read_only=True)
    class Meta:
        model = TrainingModule
        fields = ["id", "title", "description", "resources"]

class TrainerSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)
    class Meta:
        model = Trainer
        fields = ["id", "name", "email", "modules"]
