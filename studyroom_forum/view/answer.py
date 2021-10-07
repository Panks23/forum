from django.db.models.query_utils import Q
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from studyroom_forum.serializer import *
from studyroom_forum.models import *
from studyroom_forum.serializer.AnswerSerializer import AnswerSerializer


@api_view(['GET', 'POST'])
def answer_get_or_post(request, quesId):
    if request.method == 'GET':
        answer  =  Answer.objects.filter(que_id = quesId)
        serializer = AnswerSerializer(answer, many=True)
        return Response(serializer.data)
    else:
        request.data["que_id"] = quesId
        print(request.data)
        serializer = AnswerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE', 'PUT', 'GET'])
def answer_delete_or_put_or_get_by_id(request, quesId, ansId):
    if request.method == 'DELETE':
        Answer.objects.filter(pk=ansId).delete()
        return Response(status = status.HTTP_200_OK)
    elif request.method == 'GET':
        answer = Answer.objects.get(pk = ansId)
        serializer = AnswerSerializer(answer)
        return Response(serializer.data)
    else:
        obj = Answer.objects.get(pk = ansId)
        serializer = AnswerSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
