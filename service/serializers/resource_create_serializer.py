from rest_framework import serializers


class ResourceCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    file = serializers.FileField()
    module_ids = serializers.ListField(child=serializers.IntegerField(), min_length=1)
