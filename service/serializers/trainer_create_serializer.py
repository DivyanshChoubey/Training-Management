from rest_framework import serializers


class TrainerCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=False, allow_blank=True)
    email = serializers.EmailField()
