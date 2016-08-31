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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    latitude = models.CharField(max_length=20, verbose_name=_('Latitud'))
    longitude = models.CharField(max_length=20, verbose_name=_('Longitud'))

    def __str__(self):
        return "%s" % self.user.username
        
    def get_recommendations(self):
        # get answers given by the current user
        answers = self.user.answer_set.all()

        # get choices in those answers
        choices = []

        for answer in answers:
            choices.append(answer.choice)

        # get recommendations of those choices
        recommendations = []

        for choice in choices:
            recommendations += choice.recommendation_set.all()

        return recommendations

    class Meta:
        verbose_name = _('Perfil de Usuario')
        verbose_name_plural = _('Perfiles de Usuario')


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
        return "%s : %s" % (self.question.text, self.text)

    class Meta:
        verbose_name = _('Opción')
        verbose_name_plural = _('Opciones')


class Answer(models.Model):
    choice = models.ForeignKey(Choice, verbose_name=_('Opción'))
    user = models.ForeignKey(User, verbose_name=_('Usuario'))
    date_time = models.DateTimeField(default=datetime.datetime.now,
                                     verbose_name=_('Fecha y hora'))

    def __str__(self):
        return '%s : %s ' % (self.user.username, self.choice)

    class Meta:
        verbose_name = _('Respuesta')
        verbose_name_plural = _('Respuestas')


class Tip(models.Model):
    text = models.TextField(verbose_name=_('Texto'))

    def __str__(self):
        return "%s" % self.text

    class Meta:
        verbose_name = _('Tip')
        verbose_name_plural = _('Tips')


class Recommendation(models.Model):
    text = models.TextField(verbose_name=_('Texto'))
    category = models.ForeignKey(Category, verbose_name=_('Categoría'))
    choice = models.ForeignKey(Choice, verbose_name=_('Opción'), null=True)

    def __str__(self):
        return "%s" % self.text

    class Meta:
        verbose_name = _('Recomendación')
        verbose_name_plural = _('Recomendaciones')

    def applies_to(self, score):
        return score <= self.score_upper_bound
