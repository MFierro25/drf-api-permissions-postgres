from typing import List
from rest_framework import generics
from .models import List
from .serializers import ListSerializer

class TodoList(generics.ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    
class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
