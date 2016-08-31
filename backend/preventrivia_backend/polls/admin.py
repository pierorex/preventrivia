from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Poll, Question, Category, Choice, Recommendation, Answer, \
    Tip, Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class ChoiceInline(admin.TabularInline):
    model = Choice


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    inlines = [ChoiceInline]


class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )



admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Poll)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Category)
admin.site.register(Recommendation)
admin.site.register(Answer)
admin.site.register(Tip)
