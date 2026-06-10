import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from service.constants import ResponseMessage
from service.models import Trainer
from service.serializers import TrainerCreateSerializer


class TrainerCreateView(APIView):
    def post(self, request):
        serializer = TrainerCreateSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {
                    "success": False,
                    "message": ResponseMessage.INVALID_DATA,
                    "error": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        email = serializer.validated_data['email']
        name = serializer.validated_data.get("name", "").strip()

        if Trainer.objects.filter(email=email).exists():
            return Response(
                {
                    "success": False,
                    "message": ResponseMessage.EMAIL_ALREADY_EXIST
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if not name:
            try:
                response = requests.get("https://jsonplaceholder.typicode.com/users", timeout=5)
                users = response.json()
                
                matched_user = None
                for user in users:
                    if user['email'].lower() == email.lower():
                        matched_user = user
                        break

                if not matched_user:
                    return Response(
                        {
                            "success": False,
                            "message": ResponseMessage.EMAIL_NOT_FOUND
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )
                name = matched_user["name"]
            except requests.exceptions.ConnectionError:
                return Response(
                    {
                        "success": False,
                        "message": ResponseMessage.SERVICE_UNAVAILABLE
                    },
                    status=status.HTTP_503_SERVICE_UNAVAILABLE
                )
            except Exception as e:
                return Response(
                    {
                        "success": False,
                        "message": ResponseMessage.SOMETHING_WRONG
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        Trainer.objects.create(
            name = name,
            email = email
        )
        return Response(
            {
                "success": True,
                "message": ResponseMessage.TRAINER_CREATED
            },
            status=status.HTTP_201_CREATED
        )
