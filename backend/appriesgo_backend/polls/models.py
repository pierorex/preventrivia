import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Poll(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('Nombre'))

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = _('Encuesta')
        verbose_name_plural = _('Encuestas')


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Nombre'))

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = _('Categoria')
        verbose_name_plural = _('Categorias')


class Question(models.Model):
    text = models.CharField(max_length=300, verbose_name=_('Texto'))
    poll = models.ForeignKey(Poll, verbose_name=_('Encuesta'))
    category = models.ForeignKey(Category, verbose_name=_('Categoria'))

    def __str__(self):
        return "%s" % self.text

    class Meta:
        verbose_name = _('Pregunta')
        verbose_name_plural = _('Preguntas')


class Choice(models.Model):
    text = models.CharField(max_length=200, verbose_name=_('Texto'))
    value = models.IntegerField(verbose_name=_('Valor'))
    question = models.ForeignKey(Question, verbose_name=_('Pregunta'))

    def __str__(self):
        return "%s :: %s" % (self.question.text, self.text)

    class Meta:
        verbose_name = _('Opcion')
        verbose_name_plural = _('Opciones')


class Answer(models.Model):
    question = models.ForeignKey(Question, verbose_name=_('Pregunta'))
    choice = models.ForeignKey(Choice, verbose_name=_('Opcion'))
    user = models.ForeignKey(User, verbose_name=_('Usuario'))
    date_time = models.DateTimeField(default=datetime.datetime.now,
                                     verbose_name=_('Fecha y hora'))

    def __str__(self):
        return "%s : %s : %s" % (self.user.username, self.question.text,
                                 self.choice.text)

    class Meta:
        verbose_name = _('Respuesta')
        verbose_name_plural = _('Respuestas')


class Recommendation(models.Model):
    text = models.TextField(verbose_name=_('Texto'))
    category = models.ForeignKey(Category, verbose_name=_('Categoria'))
    score_upper_bound = models.IntegerField(verbose_name=
                                            _('Cota supervior de puntaje'))

    def __str__(self):
        return "%s" % self.text

    class Meta:
        verbose_name = _('Recomendacion')
        verbose_name_plural = _('Recomendaciones')
