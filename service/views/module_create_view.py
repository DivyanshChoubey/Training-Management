from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from service.constants import ResponseMessage
from service.models import Trainer, TrainingModule
from service.serializers import ModuleCreateSerializer


class ModuleCreateView(APIView):
    def post(self,request):
        serializer = ModuleCreateSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {
                    "success": False,
                    "message": ResponseMessage.INVALID_DATA
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        title = serializer.validated_data.get("title")
        description = serializer.validated_data.get("description", "")
        trainer_id = serializer.validated_data.get("trainer_id")

        try:
            trainer = Trainer.objects.get(id=trainer_id)
        except Trainer.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": ResponseMessage.TRAINER_NOT_FOUND
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        TrainingModule.objects.create(
            title=title,
            description=description,
            created_by=trainer
        )
        return Response(
            {
                "success": True,
                "message": ResponseMessage.MODULE_CREATED
            },
            status=status.HTTP_201_CREATED
        )
