from django.db.models import fields
from rest_framework import serializers
from studyroom_forum.models import *


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ( "id" ,"description", "created_by", "updated_by", "version", "que_id")
    def create(self, validated_data):
        quesId = validated_data.pop("que_id")
        print(validated_data)
        question = Question.objects.get(pk=quesId)
        article_instance = Answer.objects.create(**validated_data, que_id = question)
        return article_instance