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


class Question(models.Model):
    text = models.CharField(max_length=300)
    poll = models.ForeignKey(Poll)
    category = models.ForeignKey(Category)

    def __str__(self):
        return "%s" % self.text


class Choice(models.Model):
    text = models.CharField(max_length=200)
    value = models.IntegerField()
    question = models.ForeignKey(Question)

    def __str__(self):
        return "%s :: %s" % (self.question.text, self.text)


class Answer(models.Model):
    question = models.ForeignKey(Question)
    choice = models.ForeignKey(Choice)
    user = models.ForeignKey(User)
    date_time = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return "%s : %s : %s" % (self.user.username, self.question.text,
                                 self.choice.text)


class Recommendation(models.Model):
    text = models.TextField()
    category = models.ForeignKey(Category)
    score_lower_bound = models.IntegerField()

    def __str__(self):
        return "%s" % self.text
