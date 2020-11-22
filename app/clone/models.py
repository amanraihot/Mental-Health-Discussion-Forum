from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from  django.urls import reverse

class Topics(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('topics')
class Question(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    topics = models.ForeignKey(Topics,on_delete=models.SET_NULL,null=True,related_name='topic_questions')
    question = models.TextField(max_length=1000)
    time_added = models.DateTimeField(default=timezone.now())
    num_answers = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('question-detail',kwargs={'pk':self.pk})

class Answer(models.Model):
    question_url = models.ForeignKey(Question,on_delete=models.CASCADE)
    topics = models.ForeignKey(Topics,on_delete=models.SET_NULL,null=True,related_name='topic_answers')
    answered_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    time_created = models.DateTimeField(default=timezone.now())
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    answer = models.TextField()
    up_list = models.ManyToManyField(User, related_name="answer_up_list")
    down_list = models.ManyToManyField(User, related_name="answer_down_list")
    comment_list = models.ManyToManyField(User,related_name='comment_list')

    def get_absolute_url(self):
        return reverse('home')

class Comments(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    answer_url = models.ForeignKey(Answer,on_delete=models.CASCADE)
    date_created =models.DateTimeField(default=timezone.now())
    comments = models.TextField()

    def get_absolute_url(self):
        return reverse('home')
