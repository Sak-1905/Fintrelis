from django.shortcuts import render

# Create your views here.
import logging
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

logger = logging.getLogger(__name__)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        logger.info("Creating a new post.")
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        logger.info(f"Retrieving post with id {kwargs['pk']}.")
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        logger.info(f"Updating post with id {kwargs['pk']}.")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        logger.info(f"Deleting post with id {kwargs['pk']}.")
        return super().destroy(request, *args, **kwargs)