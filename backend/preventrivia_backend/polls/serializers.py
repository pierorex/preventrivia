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


class SimpleChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice


class QuestionSerializer(serializers.ModelSerializer):
    choice_set = SimpleChoiceSerializer(read_only=True, many=True)
    category = serializers.StringRelatedField()

    class Meta:
        model = Question


class SimpleQuestionSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    
    class Meta:
        model = Question


class ChoiceSerializer(serializers.ModelSerializer):
    question = SimpleQuestionSerializer()

    class Meta:
        model = Choice


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category


class TipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip
