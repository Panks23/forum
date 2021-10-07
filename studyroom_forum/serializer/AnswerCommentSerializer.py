from django.db.models import fields
from rest_framework import serializers
from studyroom_forum.models import *



class AnswerCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerComments
        fields = ("comment", "answer_id", "created_by", "updated_by", "version")