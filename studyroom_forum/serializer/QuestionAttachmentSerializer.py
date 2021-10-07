from django.db.models import fields
from rest_framework import serializers
from studyroom_forum.models import *


class QuestionAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAttachment
        fields = ("file_url", "question_id", "created_by", "updated_by", "version")
