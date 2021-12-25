from rest_framework import serializers
from .models import CustomUser 

class CustomUserSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(
    #     required=True
    # )
    # username = serializers.CharField()
    # password = serializers.CharField(min_length=8, write_only=True)

    class Meta:   # what is this Meta?
        model = CustomUser  
        fields = ('email', 'username', 'password', 'branch', )
        extra_kwargs = {'password': {'write_only': True}}  # what is extra_kwargs


    def create(self, validated_data):
        password = validated_data.pop('password', None)  # what it's doing 
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this, but which field
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
