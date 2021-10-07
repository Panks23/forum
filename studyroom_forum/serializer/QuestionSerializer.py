from django.db.models import fields
from rest_framework import serializers
from studyroom_forum.models import *


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("id", "name", "description", "created_by", "updated_by", "version")
