from django.contrib import admin

from edtech.models import Question, Choice, QuestionTestSeries, SeriesType, UserQuestionAnswer, Subject, Topic
from edtech.models.test_series import TestSeries


class ChoiceAdmin(admin.TabularInline):
    model = Choice
    max_num = 5
    min_num = 4
    extra = 0
    can_delete = True


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['description', 'diagram', 'difficulty_level', 'marks']

    inlines = (ChoiceAdmin,)

    class Meta:
        model = Question
        fields = '__all__'


class QuestionTestSeriesAdmin(admin.ModelAdmin):
    list_display = ['question', 'test_series']

    class Meta:
        model = QuestionTestSeries
        fields = '__all__'


class SeriesTypeAdmin(admin.ModelAdmin):
    list_display = ['series_type']

    class Meta:
        model = SeriesType
        fields = '__all__'


class UserQuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ['is_correct', 'choice', 'question', 'user']

    class Meta:
        model = UserQuestionAnswer
        fields = '__all__'


class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        model = Subject
        fields = '__all__'


class TopicAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject']

    class Meta:
        model = Topic
        fields = '__all__'


class TestSeriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'series_type', 'is_paid']

    class Meta:
        model = TestSeries
        fields = '__all__'


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(SeriesType, SeriesTypeAdmin)
admin.site.register(TestSeries, TestSeriesAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionTestSeries, QuestionTestSeriesAdmin)
admin.site.register(UserQuestionAnswer, UserQuestionAnswerAdmin)
