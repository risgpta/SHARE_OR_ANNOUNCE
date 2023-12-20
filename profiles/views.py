from django.http.multipartparser import MultiPartParser

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from profiles.models import Profiles
from profiles.serializers import ProfileSerializer
from django.http.response import JsonResponse
from rest_framework.response import Response
from django.forms.models import model_to_dict


class ProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profiles.objects.all()

    @action(detail=False, methods=['get'])
    def get_profiles(self, request):
        profiles = Profiles.objects.all()
        serializer = self.serializer_class(profiles, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK,safe=False)
        # profiles = self.get_queryset()
        # data = [ model_to_dict(p) for p in profiles]
        # response = {'data': data}
        # return Response(response)

    @action(detail=False, methods=['post'])
    def create_profile(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED,safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST,safe=False)

