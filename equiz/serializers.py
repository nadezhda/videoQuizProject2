from rest_framework import serializers
from equiz.models import *
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('answer', 'is_answer_correct')


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'quiz_type', 'question', 'answers', 'markerTime', 'replayTime', 'value', 'penalty', 'feedback', 'hint')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    #sections = serializers.PrimaryKeyRelatedField(many=True)
    sections = serializers.HyperlinkedRelatedField(many=True, view_name='section-detail')

    class Meta:
        model = User
        fields = ('url', 'username', 'sections')


class SectionSerializer(serializers.ModelSerializer):
    owner = serializers.Field(source='owner.username')
    questions = QuestionSerializer(many=True)
    # content = serializers.HyperlinkedIdentityField(view_name='section-content', format='html')

    class Meta:
        model = Section
        fields = ('id', 'title', 'category', 'owner', 'description', 'video_url', 'questions')
        # fields = ('id', 'title', 'category', 'owner', 'description', 'video_url')
        depth = 5