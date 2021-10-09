from functools import partial
from django.db.models.query_utils import Q
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from studyroom_forum.serializer import *
from studyroom_forum.models import *
from studyroom_forum.serializer.AnswerAttachmentSerializer import AnswerAttachmentSerializer
from studyroom_forum.serializer.AnswerSerializer import AnswerSerializer
from studyroom_forum.pagination import *
from studyroom_forum.response import *


@api_view(['GET', 'POST'])
def answer_get_or_post(request, quesId):
    if request.method == 'GET':
        paginator = StandardResultsSetPagination()
        question  =  Answer.objects.filter(que_id = quesId)
        result_page = paginator.paginate_queryset(question, request)
        serializer = AnswerSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    else:
        request.data["que_id"] = quesId
        serializer = AnswerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE', 'PUT', 'GET'])
def answer_delete_or_put_or_get_by_id(request, quesId, ansId):
    if request.method == 'DELETE':
        try:
            Answer.objects.filter(pk=ansId, que_id = quesId).delete()
            return Response(getGenericResponse("Successfully deleted the answer", None), status = status.HTTP_200_OK)
        except:
            return Response(getGenericResponse("Please pass valid question/ans id", None), status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        try:
            Question.objects.get(pk = quesId)
            answer = Answer.objects.get(pk = ansId, que_id = quesId)
            serializer = AnswerSerializer(answer)
            return Response(getGenericResponse("Successfully Fetched the data", serializer.data))
        except:
            return Response(getGenericResponse("Please pass valid question/ans id", None), status = status.HTTP_400_BAD_REQUEST)
    else:
        try:
            obj = Answer.objects.get(pk = ansId, que_id = quesId)
            serializer = AnswerSerializer(obj, data=request.data, partial= True)
            if serializer.is_valid():
                serializer.save()
                return Response(getGenericResponse("Successfully update the answer",serializer.data), status=status.HTTP_202_ACCEPTED)
        except:
            return Response(getGenericResponse("Please pass valid question/ans id", None), status = status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["POST", "GET"])
def answer_attachment_post_or_get(request, ansId):
    if request.method == 'GET':
        paginator = StandardResultsSetPagination()
        answer  =  AnswerAttachment.objects.filter(answer_id = ansId)
        result_page = paginator.paginate_queryset(answer, request)
        serializer = AnswerAttachmentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    else:
        validated_data_for_attachement = list()
        for data in request.data["attachment"]:
            attachment = dict()
            attachment["answer_id"] = ansId
            attachment["file_url"] = data["file_url"]
            attachment["created_by"] = 2
            attachment["updated_by"] = 2
            validated_data_for_attachement.append(attachment)
        serializer = AnswerAttachmentSerializer(data=validated_data_for_attachement, many = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def answer_attachment_delete(request, ansId, attachementId):
    try:
        Answer.objects.get(pk = ansId)
    except:
        return Response(getGenericResponse("Please pass valid answer id", None), status = status.HTTP_400_BAD_REQUEST)
    AnswerAttachment.objects.filter(pk=attachementId, answer_id = ansId).delete()
    return Response(getGenericResponse("Successfully deleted the data", None), status = status.HTTP_200_OK) 
