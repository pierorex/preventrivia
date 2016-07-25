import datetime
from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return "%s" % self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % self.name


class Choice(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return "Answer to question %d :: %s" % (self.question.pk, self.text)


class Question(models.Model):
    text = models.CharField(max_length=300)
    poll = models.ForeignKey(Poll)
    category = models.ForeignKey(Category)
    choices = models.ManyToManyField(Choice, related_name='questions')

    def __str__(self):
        return "Question : %s" % self.text


class Answer(models.Model):
    question = models.ForeignKey(Question)
    choice = models.ForeignKey(Choice)
    user = models.ForeignKey(User)
    date_time = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return "Answer : %s %s %s" % (self.user.username,
                                      self.question.text[:10],
                                      self.choice.text[:10])


class Recommendation(models.Model):
    text = models.TextField()
    category = models.ForeignKey(Category)
    score_lower_bound = models.IntegerField()

    def __str__(self):
        return "%s" % self.text[:20]
