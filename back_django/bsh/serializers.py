from rest_framework import serializers  
from bsh.models import Bsh

class BshSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bsh
        fields = ('id','title','author','pw','content')


    def create(self, validated_data):
        return Bsh.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.pw = validated_data.get('pw', instance.pw)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
