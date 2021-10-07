from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(QuestionAttachment)
admin.site.register(AnswerAttachment)
admin.site.register(AnswerComments)

