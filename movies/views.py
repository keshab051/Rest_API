from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Movieserializers
from .models import Moviedata
 
# view to display the seriaized data 
class MovieViewSet(viewsets.ModelViewSet):   
    queryset = Moviedata.objects.all()
    serializer_class = Movieserializers


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='action')
    serializer_class = Movieserializers

class ComedyViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ = 'comedy')
    serializer_class = Movieserializers