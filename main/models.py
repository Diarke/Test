from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Questions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    questions = models.TextField()

    def __str__(self):
        return self.questions
    

class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer
    

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)
    total = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    

class News(models.Model):
    author = models.CharField(max_length=200)
    popularity = models.BooleanField(default=False)
    category = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)
    img1 = models.ImageField(upload_to='upload', blank=True, null=True)
    img2 = models.ImageField(upload_to='upload', blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
    
    def get_absolute_url(self):
        return f'/news/{self.pk}'
    


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=30)
    text = models.TextField(max_length=250)


    def __str__(self):
        return self.name
    