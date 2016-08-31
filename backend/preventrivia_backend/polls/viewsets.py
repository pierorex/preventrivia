from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView, status
from rest_framework.permissions import AllowAny
from .models import Poll, Question, Recommendation, Category, Choice, Answer, \
    Tip
from .serializers import PollSerializer, QuestionSerializer, \
    RecommendationSerializer, CategorySerializer, ChoiceSerializer, \
    AnswerSerializer, TipSerializer


class PollViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class RecommendationViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class TipViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = Tip.objects.all()
    serializer_class = TipSerializer


class AnswerUserView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request, *args, **kwargs):
        try:
            user = request.data.get('user', None)
            question = request.data.get('question', None)
            try:
                answerData = (Answer.objects
                                    .filter(user=user)
                                    .filter(question=question))[0]
                answerData = {'id': answerData.id,
                              'choice': answerData.choice.id}
            except:
                answerData = {'id': -1,
                              'response': 'Answer does not exist'}

            return Response(answerData, status.HTTP_200_OK)

        except:  # User does not exist
            return Response({request},
                            status.HTTP_412_PRECONDITION_FAILED)
