from django.db.models.query_utils import Q
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from studyroom_forum.serializer import *
from studyroom_forum.models import *
from studyroom_forum.serializer.AnswerCommentSerializer import AnswerCommentSerializer


@api_view(['GET', 'POST'])
def comment_get_or_post(request, quesId,  ansId):
    if request.method == 'GET':
        comment  =  AnswerCommentSerializer.objects.filter(que_id = quesId)
        serializer = AnswerCommentSerializer(comment, many=True)
        return Response(serializer.data)
    else:
        request.data["ans_id"] = ansId
        serializer = AnswerCommentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE', 'PUT', 'GET'])
def comment_delete_or_put_or_get(request, quesId,  ansId, commentId):
    if request.method == 'DELETE':
        AnswerComments.objects.filter(pk=commentId).delete()
        return Response(status = status.HTTP_200_OK)
    elif request.method == 'GET':
        comment = AnswerComments.objects.get(pk = commentId)
        serializer = AnswerCommentSerializer(comment)
        return Response(serializer.data)
    else:
        obj = AnswerComments.objects.get(pk = commentId)
        serializer = AnswerCommentSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
