from django.db.models import fields
from rest_framework import serializers
from studyroom_forum.models import *


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("id", "name", "description", "created_by", "updated_by")
    def create(self, validated_data):
        validated_data["version"] = 1
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        Question.objects.filter(pk=instance.id).update(**validated_data)
        return instance
