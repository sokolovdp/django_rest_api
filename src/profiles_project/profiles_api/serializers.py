from rest_framework import serializers

from profiles_api import models

class NameSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):   # create and return new user
        user = models.UserProfile(
            email=validated_data['email'].lower(),
            name=validated_data['name'],
            )
        user.set_password(validated_data['password'])
        user.save()
        return user



class ProfileFeedItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}

    
