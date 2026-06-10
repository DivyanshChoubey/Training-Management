from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from service.constants import ResponseMessage
from service.models import Trainer
from service.serializers.trainer_detail_serializer import TrainerSerializer


class TrainerListView(APIView):
    def get(self, request):
        trainers = Trainer.objects.all()

        return Response({
            "success": True,
            "data": TrainerSerializer(trainers, many=True).data
        }, status=status.HTTP_200_OK)


class TrainerDetailView(APIView):
    def get(self, request, pk):

        try:
            trainer = Trainer.objects.prefetch_related(
                'modules__resources'
            ).get(id=pk)
        except Trainer.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": ResponseMessage.TRAINER_NOT_FOUND
                },
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            {
                "success": True,
                "data": TrainerSerializer(trainer).data
            },
            status=status.HTTP_200_OK
        )
