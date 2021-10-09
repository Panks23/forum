from django.http import response
from rest_framework import status
from rest_framework.decorators import api_view
from studyroom_forum.decorators import authorized_user
from rest_framework.response import Response
from studyroom_forum.serializer import *
from studyroom_forum.models import *
from studyroom_forum.serializer.QuestionSerializer import QuestionSerializer
from studyroom_forum.serializer.QuestionAttachmentSerializer import QuestionAttachmentSerializer
from studyroom_forum.pagination import *
from studyroom_forum.response import *


@api_view(['GET', 'POST'])
@authorized_user
def question_get_or_post(request):
    if request.method == 'GET':
        paginator = StandardResultsSetPagination()
        question  =  Question.objects.all()
        result_page = paginator.paginate_queryset(question, request)
        serializer = QuestionSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    else:
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', 'PUT', 'GET'])
@authorized_user
def question_delete_or_put_or_get_by_id(request, quesId):
    if request.method == 'DELETE':
        Question.objects.filter(pk=quesId).delete()
        return Response(getGenericResponse("Successfully deleted the data", None), status = status.HTTP_200_OK)
    elif request.method == 'GET':
        try:
            question = Question.objects.get(pk = quesId)
        except:
            return Response(getGenericResponse("Please pass valid question id"), status = status.HTTP_400_BAD_REQUEST)
        serializer = QuestionSerializer(question)
        return Response(getGenericResponse("Successfully fetched the data", serializer.data),status = status.HTTP_200_OK)
    else:
        try:
            obj = Question.objects.get(pk = quesId)
            serializer = QuestionSerializer(obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(getGenericResponse("Successfully updated the data", None), status=status.HTTP_202_ACCEPTED)
        except:
            return Response(getGenericResponse("Failed to update question"), status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["POST", "GET"])
@authorized_user
def question_attachment_post_or_get(request, quesId):
    if request.method == 'GET':
        paginator = StandardResultsSetPagination()
        question  =  QuestionAttachment.objects.filter(question_id = quesId)
        result_page = paginator.paginate_queryset(question, request)
        serializer = QuestionAttachmentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    else:
        validated_data_for_attachement = list()
        for data in request.data["attachment"]:
            attachment = dict()
            attachment["question_id"] = quesId
            attachment["file_url"] = data["file_url"]
            attachment["created_by"] = 2
            attachment["updated_by"] = 2
            validated_data_for_attachement.append(attachment)
        serializer = QuestionAttachmentSerializer(data=validated_data_for_attachement, many = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
@authorized_user
def question_attachment_delete(request, quesId, attachementId):
    try:
        question = Question.objects.get(pk = quesId)
    except:
        return Response(getGenericResponse("Please pass valid question id", None), status = status.HTTP_400_BAD_REQUEST)
    QuestionAttachment.objects.filter(pk=attachementId, question_id = quesId).delete()
    return Response(getGenericResponse("Successfully deleted the data", None), status = status.HTTP_200_OK) 
