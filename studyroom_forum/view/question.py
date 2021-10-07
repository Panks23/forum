from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from studyroom_forum.serializer import *
from studyroom_forum.models import *
from studyroom_forum.serializer.QuestionSerializer import QuestionSerializer


@api_view(['GET', 'POST'])
def question_get_or_post(request):
    if request.method == 'GET':
        question  =  Question.objects.all()
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)
    else:
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', 'PUT', 'GET'])
def question_delete_or_put_or_get_by_id(request, quesId):
    if request.method == 'DELETE':
        Question.objects.filter(pk=quesId).delete()
        return Response(status = status.HTTP_200_OK)
    elif request.method == 'GET':
        question = Question.objects.get(pk = quesId)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)
    else:
        obj = Question.objects.get(pk = quesId)
        serializer = QuestionSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
