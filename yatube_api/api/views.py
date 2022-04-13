from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters, mixins

from .permissions import IsAuthorOrReadOnly
from posts.models import Post, Group, Comment, Follow
from .serializers import PostSerializer, GroupSerializer, CommentSerializer, FollowSerializer



class CreateListViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin ,
                            viewsets.GenericViewSet):
    pass


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = None


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]
    pagination_class = None

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        comments = Comment.objects.filter(post_id=post.id)
        return comments

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(post_id=post.id, author=self.request.user)


class FollowViewSet(CreateListViewSet):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsAuthorOrReadOnly]
    pagination_class = None
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username',)

    def get_queryset(self):
        follow = Follow.objects.filter(user=self.request.user)
        return follow
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)