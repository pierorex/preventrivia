from rest_framework import serializers
from .models import Question, Poll, Choice, Answer, Category, Recommendation, \
    Tip


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category


class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation


class TipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip
