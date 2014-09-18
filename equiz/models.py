from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.name


# class Video(models.Model):
#     url = models.URLField(blank=True, null=True)
#
#     def __unicode__(self):
#         return self.url

class Section(models.Model):
    title = models.CharField(max_length=128, blank=False)
    owner = models.ForeignKey('auth.User', related_name='sections')
    category = models.ForeignKey(Category, blank=False)
    description = models.TextField(blank=True)
    video_url = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.title


class QuestionType(models.Model):
    type = models.CharField(max_length=128, blank=False)

    def __unicode__(self):
        return self.type


class Question(models.Model):
    quiz_type = models.ForeignKey(QuestionType, blank=False)
    section = models.ForeignKey(Section, related_name='questions', blank=False, null=False)
    question = models.CharField(max_length=500, blank=False)
    markerTime = models.IntegerField(null=True, blank=True)
    replayTime = models.IntegerField(null=True, blank=True)
    value = models.FloatField(null=True, blank=True, default=0.0)
    penalty = models.FloatField(null=True, blank=True, default=0.0)
    feedback = models.CharField(max_length=300, blank=True, default='Correct')
    hint = models.CharField(max_length=300, blank=True, default='Incorrect')

    def __unicode__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', blank=False)
    answer = models.CharField(max_length=300, blank=False)
    is_answer_correct = models.BooleanField(default=False)

    def __unicode__(self):
        return self.answer




