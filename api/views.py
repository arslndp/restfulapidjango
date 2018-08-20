from django.shortcuts import render

# Create your views here.
from .models import Album,Song
from rest_framework import viewsets
from .serializers import AlbumSerializer, SongSerializer

class AlbumViewSet(viewsets.ModelViewSet):
	queryset =  Album.objects.all()
	serializer_class = AlbumSerializer
	
class SongViewSet(viewsets.ModelViewSet):
	queryset = Song.objects.all()
	serializer_class = SongSerializer

def index(request):
	return render(request,'public/index.html',{})