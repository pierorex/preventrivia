from rest_framework import serializers
from .models import Question, Poll, Choice, Answer, Category, Recommendation, \
    Tip


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer


class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice


class QuestionSerializer(serializers.ModelSerializer):
    choice_set = ChoiceSerializer(read_only=True, many=True)

    class Meta:
        model = Question


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category


class TipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip
