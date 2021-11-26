from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Follow, Group, Post, User

SUBSCRIBE_TO_YOURSELF = 'Вы не можете подписаться на самого себя'


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='username', read_only=True,
                            default=serializers.CurrentUserDefault())
    following = SlugRelatedField(slug_field='username',
                                 queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = '__all__'
        validators = [serializers.UniqueTogetherValidator(
            queryset=Follow.objects.all(), fields=('user', 'following'))]

    def validate_following(self, value):
        if value == self.context.get('request').user:
            raise serializers.ValidationError(SUBSCRIBE_TO_YOURSELF)
        return value
