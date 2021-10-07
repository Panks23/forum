from django.db.models import fields
from rest_framework import serializers
from studyroom_forum.models import *



class AnswerAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerAttachment
        fields = ("file_url", "answer_id", "created_by", "updated_by", "version")