from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, User
from django.utils.translation import gettext_lazy as _

from .models import Choice, Course, Instructor, Learner, Lesson, Question, Submission


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "pub_date")
    search_fields = ("question_text",)
    inlines = [ChoiceInline]


class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    search_fields = ("title",)
    ordering = ("order",)


admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)

admin.site.register(User, UserAdmin)
admin.site.register(Group)

admin.site.site_header = _("OnlineCourse Admin")
admin.site.site_title = _("OnlineCourse Admin Portal")
admin.site.index_title = _("Administration")
