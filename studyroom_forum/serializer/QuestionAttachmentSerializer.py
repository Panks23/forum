from django.db.models import fields
from rest_framework import serializers
from studyroom_forum.models import *


class QuestionAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAttachment
        fields = ("id", "file_url", "question_id", "created_at", "updated_at", "created_by", "updated_by")
    def create(self, validated_data):
        validated_data["version"] = 1
        quesId = validated_data.pop("question_id")
        question = Question.objects.get(pk=quesId)
        return QuestionAttachment.objects.create(**validated_data, question_id=question)
