from django.urls import path
from .view.question import *
from .view.answer import *
from .view.comment import *


urlpatterns = [
    path('studyroom/question/', question_get_or_post, name="question_get_or_post"),
    path('studyroom/question/<int:quesId>/', question_delete_or_put_or_get_by_id, name="question_delete_or_put_or_get_by_id"),
    path('studyroom/question/<int:quesId>/answer/', answer_get_or_post, name="answer_get_or_post"),
    path('studyroom/question/<int:quesId>/answer/<int:ansId>/', answer_delete_or_put_or_get_by_id, name="answer_delete_or_put_or_get_by_id"),
    path('studyroom/question/<int:quesId>/answer/<int:ansId>/comment/', comment_get_or_post, name="comment_get_or_post"),
    path('studyroom/question/<int:quesId>/answer/<int:ansId>/comment/<int:commentId>', comment_delete_or_put_or_get, name="comment_delete_or_put_or_get"),
]