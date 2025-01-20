from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Movieserializers
from .models import Moviedata
# Create your views here.


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = Movieserializers