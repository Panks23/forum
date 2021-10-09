from django.db.models import fields
from rest_framework import serializers
from studyroom_forum.models import *



class AnswerCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerComments
        fields = ("id", "comment", "answer_id", "created_by", "updated_by")
    def create(self, validated_data):
        validated_data["version"] = 1
        answer_id = validated_data.pop("answer_id")
        answer = Answer.objects.get(pk=answer_id)
        return AnswerComments.objects.create(**validated_data, answer_id=answer)

    def update(self, instance, validated_data):
        validated_data.pop("created_by")
        AnswerComments.objects.filter(pk=instance.id).update(**validated_data)
        return instance