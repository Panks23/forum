from django.db.models import fields
from rest_framework import serializers
from studyroom_forum.models import *



class AnswerAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerAttachment
        fields = ("id","file_url", "answer_id", "created_by", "updated_by")
    def create(self, validated_data):
        validated_data["version"] = 1
        answer_id = validated_data.pop("answer_id")
        answer = Answer.objects.get(pk=answer_id)
        return AnswerAttachment.objects.create(**validated_data, answer_id=answer)