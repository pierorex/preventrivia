import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Poll(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('Name'))

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = _('Poll')
        verbose_name_plural = _('Polls')


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Name'))

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Question(models.Model):
    text = models.CharField(max_length=300, verbose_name=_('Text'))
    poll = models.ForeignKey(Poll, verbose_name=_('Poll'))
    category = models.ForeignKey(Category, verbose_name=_('Category'))

    def __str__(self):
        return "%s" % self.text

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')


class Choice(models.Model):
    text = models.CharField(max_length=200, verbose_name=_('Text'))
    value = models.IntegerField(verbose_name=_('Value'))
    question = models.ForeignKey(Question, verbose_name=_('Question'))

    def __str__(self):
        return "%s :: %s" % (self.question.text, self.text)

    class Meta:
        verbose_name = _('Choice')
        verbose_name_plural = _('Choices')


class Answer(models.Model):
    question = models.ForeignKey(Question, verbose_name=_('Question'))
    choice = models.ForeignKey(Choice, verbose_name=_('Choice'))
    user = models.ForeignKey(User, verbose_name=_('User'))
    date_time = models.DateTimeField(default=datetime.datetime.now,
                                     verbose_name=_('Date and time'))

    def __str__(self):
        return "%s : %s : %s" % (self.user.username, self.question.text,
                                 self.choice.text)

    class Meta:
        verbose_name = _('Answer')
        verbose_name_plural = _('Answers')


class Recommendation(models.Model):
    text = models.TextField(verbose_name=_('Text'))
    category = models.ForeignKey(Category, verbose_name=_('Category'))
    score_lower_bound = models.IntegerField(verbose_name=_('Score lower bound'))

    def __str__(self):
        return "%s" % self.text

    class Meta:
        verbose_name = _('Recommendation')
        verbose_name_plural = _('Recommendations')
