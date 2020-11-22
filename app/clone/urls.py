from django.urls import path,include
from .import views
from .views import (AddQuestionView,AddAnswerView,QuestionUpdateView,AnswerUpdateView,
                UpvoteCreateView,QuestionDeleteView,AnswerDeleteView,QuestionDetailView,
                AnswerDetailView,CommentCreateView,LatestFeedView,QuestionListView,
                QuestionsAnswer,FollowFromAnswers,TopicCreateView,TopicListView,
                QuestionByTopics,AnswerByTopics
            )
urlpatterns = [
    path('',LatestFeedView.as_view(),name='home'),
    path('addQuestion/<int:pk>',AddQuestionView.as_view(),name='add-question'),
    path('question/<int:pk>/answer',AddAnswerView.as_view(),name='add-answer'),
    path('question/update/<int:pk>', QuestionUpdateView.as_view(), name='update-question'),
    path('answer/update/<int:pk>', AnswerUpdateView.as_view(), name='update-answer'),
    path('answer/upvote/<int:pk>', UpvoteCreateView.as_view(), name='upvote'),
    path('question/<int:pk>/delete', QuestionDeleteView.as_view(), name='question-delete'),
    path('answer/<int:pk>/delete',AnswerDeleteView.as_view(), name='answer-delete'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('answer/<int:pk>/', AnswerDetailView.as_view(), name='answer-detail'),
    path('answer/<int:pk>/comment', CommentCreateView.as_view(), name='comment'),
    path('questions/', QuestionListView.as_view(), name='questions'),
    path('questions/answer/<int:pk>', QuestionsAnswer.as_view(), name='questions-answers'),
    path('follow/answer/<int:pk>', views.FollowFromAnswers, name='follow-answer'),
    path('create/topic', TopicCreateView.as_view(), name='create_topic'),
    path('topics', TopicListView.as_view(), name='topics'),
    path('question/byTopics/<int:pk>/', views.QuestionByTopics, name='topics_questions'),
    path('answers/byTopics/<int:pk>/', views.AnswerByTopics, name='topics_answers'),

]