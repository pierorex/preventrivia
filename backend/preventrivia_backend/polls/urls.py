from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .viewsets import AnswerViewSet, ChoiceViewSet, QuestionViewSet, \
    RecommendationViewSet, CategoryViewSet, PollViewSet, TipViewSet, \
    AnswerUserView

# Router for RESTful API
rest_router = DefaultRouter()
rest_router.register(r'answer', AnswerViewSet)
rest_router.register(r'choice', ChoiceViewSet)
rest_router.register(r'question', QuestionViewSet)
rest_router.register(r'recommendation', RecommendationViewSet)
rest_router.register(r'category', CategoryViewSet)
rest_router.register(r'poll', PollViewSet)
rest_router.register(r'tip', TipViewSet)

urlpatterns = [
	url(r'^answerUser$', AnswerUserView.as_view(), name='answerUser'),
    url(r'^', include(rest_router.urls)),
]
