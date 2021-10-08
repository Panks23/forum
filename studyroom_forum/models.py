from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.BigIntegerField()
    updated_by = models.BigIntegerField()
    version = models.IntegerField()


class Question(BaseModel):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000, null=True)



class QuestionAttachment(BaseModel):
    file_url = models.CharField(max_length=300)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)


class Answer(BaseModel):
    description = models.CharField(max_length=1000)
    que_id = models.ForeignKey(Question, on_delete=CASCADE)
    
class AnswerAttachment(BaseModel):
    file_url = models.CharField(max_length=300)
    answer_id = models.ForeignKey(Answer, on_delete=CASCADE)

class AnswerComments(BaseModel):
    comment = models.CharField(max_length=400)
    answer_id = models.ForeignKey(Answer, on_delete=CASCADE)
  
