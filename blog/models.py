from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
    
class Choice(models.Model):
    user = models.ForeignKey(User,on_delete=CASCADE)
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)
    url = models.URLField(null=True, blank=True)
    category = models.ForeignKey(Question,on_delete=CASCADE)
    choice_text = models.TextField()
    