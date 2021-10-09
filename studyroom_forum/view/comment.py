from functools import partial
from django.db.models.query_utils import Q
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from studyroom_forum.serializer import *
from studyroom_forum.models import *
from studyroom_forum.serializer.AnswerCommentSerializer import AnswerCommentSerializer
from studyroom_forum.response import *
from studyroom_forum.pagination import *
from studyroom_forum.decorators import authorized_user


@api_view(['GET', 'POST'])
@authorized_user
def comment_get_or_post(request, ansId):
    if request.method == 'GET':
        paginator = StandardResultsSetPagination()
        comment  =  AnswerComments.objects.filter(answer_id = ansId)
        result_page = paginator.paginate_queryset(comment, request)
        serializer = AnswerCommentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    else:
        request.data["answer_id"] = ansId
        serializer = AnswerCommentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE', 'PUT', 'GET'])
@authorized_user
def comment_delete_or_put_or_get(request, ansId, commentId):
    if request.method == 'DELETE':
        AnswerComments.objects.filter(pk=commentId, answer_id = ansId).delete()
        return Response(status = status.HTTP_200_OK)
    elif request.method == 'GET':
        try:
            comment = AnswerComments.objects.get(pk = commentId, answer_id = ansId)
            serializer = AnswerCommentSerializer(comment)
            return Response(getGenericResponse("Successfully fetcher comment details", serializer.data))
        except:
            return Response(getGenericResponse("Please pass valid ans/comment id", None), status = status.HTTP_400_BAD_REQUEST)

    else:
        try:
            obj = AnswerComments.objects.get(pk = commentId)
            serializer = AnswerCommentSerializer(obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(getGenericResponse("Successfully update the data", None), status=status.HTTP_202_ACCEPTED)
        except:
            return Response(getGenericResponse("Please pass valid ans/comment id", None), status = status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
