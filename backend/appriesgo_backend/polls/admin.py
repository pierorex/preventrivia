from django.contrib import admin
from .models import Poll, Question, Category, Choice, Recommendation, Answer


class QuestionInline(admin.TabularInline):
    model =


admin.site.register(Poll)
admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Choice)
admin.site.register(Recommendation)
admin.site.register(Answer)
