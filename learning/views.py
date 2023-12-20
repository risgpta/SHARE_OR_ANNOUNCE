


# myapp/views.py
from rest_framework import viewsets
from .models import Learning
from .serializers import LearningSerializer

from rest_framework.decorators import action
from rest_framework.response import Response


from rest_framework import status



# Create your views here.





class LearningViewSet(viewsets.ModelViewSet):
  queryset = Learning.objects.all()
  serializer_class = LearningSerializer

  @action(detail=False, methods=['get'])
  def get_learnings(self, request):
    queryset = self.get_queryset()
    serializer = LearningSerializer(queryset, many=True)
    return Response(serializer.data)

  @action(detail=False, methods=['post'])
  def create_learning(self, request):
      print(request.data)
      serializer = LearningSerializer(data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

