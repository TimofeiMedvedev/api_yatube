from api.permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from posts.models import Comment, Group, Post
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import CommentSerializer, GroupSerializer, PostSerializer

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated,)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly,)

    def get_post(self):
        post = Post.objects.get(id=self.kwargs.get('post_id'))
        return post

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())

    def get_queryset(self):
        return self.get_post().comments.all()
