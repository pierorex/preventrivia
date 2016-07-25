from django.contrib import admin
from .models import Poll, Question, Category, Choice, Recommendation, Answer


class ChoiceInline(admin.TabularInline):
    model = Choice


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    inlines = [ChoiceInline]


admin.site.register(Poll)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Category)
admin.site.register(Recommendation)
admin.site.register(Answer)
