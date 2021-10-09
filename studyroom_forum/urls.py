from django.urls import path
from .view.question import *
from .view.answer import *
from .view.comment import *
question_attachment_delete

urlpatterns = [
    path('athena/question/', question_get_or_post, name="question_get_or_post"),
    path('athena/question/<int:quesId>/', question_delete_or_put_or_get_by_id, name="question_delete_or_put_or_get_by_id"),
    path('athena/question/<int:quesId>/attachment', question_attachment_post_or_get, name="question_attachment_post"),
    path('athena/question/<int:quesId>/attachment/<int:attachementId>/', question_attachment_delete, name="question_attachment_delete"),
    path('athena/question/<int:quesId>/answer/', answer_get_or_post, name="answer_get_or_post"),
    path('athena/question/<int:quesId>/answer/<int:ansId>/', answer_delete_or_put_or_get_by_id, name="answer_delete_or_put_or_get_by_id"),
    path('athena/answer/<int:ansId>/attachment', answer_attachment_post_or_get, name="answer_attachment_post_or_get"),
    path('athena/answer/<int:ansId>/attachment/<int:attachementId>/', answer_attachment_delete, name="answer_attachment_delete"),
    path('athena/answer/<int:ansId>/comment/', comment_get_or_post, name="comment_get_or_post"),
    path('athena/answer/<int:ansId>/comment/<int:commentId>', comment_delete_or_put_or_get, name="comment_delete_or_put_or_get"),
]