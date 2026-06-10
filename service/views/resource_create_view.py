import os

from django.core.files.base import ContentFile
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from service.constants import ResponseMessage
from service.models import Resource, TrainingModule
from service.serializers import ResourceCreateSerializer


class ResourceCreateView(APIView):
    def post(self, request):
        serializer = ResourceCreateSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {
                    "success": False,
                    "message": ResponseMessage.INVALID_DATA,
                    "error": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        name = serializer.validated_data.get("name")
        file = serializer.validated_data.get("file")
        module_ids = serializer.validated_data.get("module_ids")
        
        for module_id in module_ids:
            if not TrainingModule.objects.filter(id=module_id).exists():
                return Response(
                    {
                        "success": False,
                        "message":ResponseMessage.MODULE_NOT_FOUND
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
        
        allowed_extensions = ['.pdf', '.docx']
        file_ext =  os.path.splitext(file.name)[1].lower()
        if file_ext not in allowed_extensions:
            return Response(
                {
                    "success": False,
                    "message": ResponseMessage.INVALID_EXT
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if file.size > 2 * 1024 * 1024:
            return Response(
                {
                    "success": False,
                    "message": ResponseMessage.INVALID_FILE_SIZE
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        first_module = TrainingModule.objects.select_related("created_by").get(id=module_ids[0])
        trainer_id = first_module.created_by.id

        different_trainer = TrainingModule.objects.filter(id__in=module_ids).exclude(created_by=trainer_id).exists()
        if different_trainer:
            return Response(
                {
                    "success": False,
                    "message": ResponseMessage.INVALID_MODULE
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        file_path = f"resources/{trainer_id}/{file.name}"
        resource = Resource(name=name)
        resource.file.save(file_path, ContentFile(file.read()), save=True)

        modules = TrainingModule.objects.filter(id__in=module_ids)
        resource.modules.set(modules)

        return Response(
            {
                "success": True,
                "message": ResponseMessage.RESOURCE_CREATED,
                "data": {
                    "id": resource.id,
                    "name": resource.name,
                    "file_path": resource.file.name,
                    "modules": list(modules.values('id', 'title'))
                }
            },
            status=status.HTTP_201_CREATED
        )
