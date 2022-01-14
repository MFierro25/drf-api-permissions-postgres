from typing import List
from rest_framework import generics
from .models import List
from .serializers import ListSerializer
from .permissions import IsAuthorOrReadOnly

class TodoList(generics.ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    
class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = List.objects.all()
    serializer_class = ListSerializer

