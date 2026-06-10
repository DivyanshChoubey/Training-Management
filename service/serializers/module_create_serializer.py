from rest_framework import serializers


class ModuleCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=200, required=False, allow_blank=True)
    trainer_id = serializers.IntegerField()
