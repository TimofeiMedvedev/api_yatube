from posts.models import Comment, Group, Post, User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='posts'
    )

    class Meta:
        model = User
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Post
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )

    class Meta:
        model = Comment
        fields = '__all__'
