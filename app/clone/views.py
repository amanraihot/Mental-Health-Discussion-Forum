from django.shortcuts import render,redirect,get_object_or_404,HttpResponse,reverse
from django.views.generic import ListView,CreateView,UpdateView,RedirectView,DeleteView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import  Question,Answer,Comments,Topics
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.urls import reverse_lazy
from users.models import Profile,Friend
from django.contrib.auth.models import User

class LatestFeedView(ListView):
    model = Answer
    context_object_name = 'answers'
    template_name = 'clone/home.html'
    ordering = ['-time_created']

class TopicCreateView(CreateView):
    model  = Topics
    fields = ['name']

class TopicListView(ListView):
    model = Topics
    context_object_name = 'topic'
    template_name = 'clone/topics_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topics'] =  Topics.objects.order_by('name')
        return context

def QuestionByTopics(request,pk):
        topics = Topics.objects.get(pk=pk)
        questions = Question.objects.filter(topics=topics)
        for que in questions:
            print(que.question)
        context = {'questions': questions,'name':topics.name}
        return render(request,'clone/topic_questions.html',context)


def AnswerByTopics(request, pk):
    topics = Topics.objects.get(pk=pk)
    answers = Answer.objects.filter(topics=topics)
    context = {'answers': answers,'name':topics.name}
    return render(request, 'clone/topic_answers.html', context)

class AddQuestionView(LoginRequiredMixin,CreateView):
    model = Question
    fields = ['question']
    def form_valid(self, form):
        topic = Topics.objects.get(pk=self.kwargs.get('pk'))
        form.instance.author = self.request.user
        form.instance.topics = topic
        return super().form_valid(form)

class AddAnswerView(LoginRequiredMixin,CreateView):
    model = Answer
    fields = ['answer']

    def form_valid(self, form):
            form.instance.answered_by = self.request.user
            question = Question.objects.get(pk=self.kwargs.get('pk'))
            topics = question.topics
            form.instance.topics = topics
            question.num_answers+=1
            question.save()
            form.instance.question_url= Question.objects.get(pk=self.kwargs.get('pk'))
            return super().form_valid(form)

class QuestionUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Question
    fields = ['question']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.author:
            return True
        return False

class AnswerUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Answer
    fields = ['answer']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ans = self.get_object()
        if self.request.user == ans.answered_by:
            return True
        return False


class UpvoteCreateView(LoginRequiredMixin,RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        answer = get_object_or_404(Answer,pk=self.kwargs.get('pk'))
        url_ = answer.get_absolute_url()
        if self.request.user not in answer.up_list.all():
            answer.up_list.add(self.request.user)
            answer.upvotes+=1
            answer.save()
            return url_



class QuestionDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Question
    success_url = reverse_lazy('home')

    def test_func(self):
        question =self.get_object()
        if self.request.user == question.author:
            return True
        return False

class AnswerDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Answer
    success_url = reverse_lazy('home')

    def test_func(self):
        ans = Answer.objects.get(pk=self.kwargs.get('pk'))
        question = ans.question_url

        if self.request.user == ans.answered_by:
            if question.num_answers == 1:
                question.num_answers = 0
            else:
                question.num_answers-=1
            question.save()
            return True
        return False

class QuestionDetailView(DetailView):
    model = Question

class AnswerDetailView(DetailView):
    model = Answer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        answer = Answer.objects.get(pk=self.kwargs.get('pk'))
        context['id'] = answer.answered_by.pk
        current_user = Profile.objects.get(user=self.request.user)
        context['following_list'] = current_user.following.all()
        context['s_id']= self.request.user.pk
        context['comments'] = Comments.objects.filter(answer_url=answer)
        return context

class CommentCreateView(LoginRequiredMixin,CreateView):
    model = Comments
    fields = ['comments']

    def form_valid(self, form):
        answer = Answer.objects.get(pk=self.kwargs.get('pk'))
        if self.request.user not in answer.up_list.all():
            answer.up_list.add(self.request.user)
            answer.save()
            form.instance.author = self.request.user
            form.instance.answer_url  = answer
            return super().form_valid(form)
        else:
            return HttpResponse('nope')


class QuestionListView(ListView):
    model= Question
    template_name = 'clone/question_list.html'
    context_object_name = 'questions'
    ordering = ['-time_added']


class QuestionsAnswer(ListView):
    model = Answer
    template_name = 'clone/question_answer.html'
    ordering = ['upvotes']

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            question = Question.objects.get(pk=self.kwargs.get('pk'))
            answer = Answer.objects.filter(question_url=question)
            context['answers'] = answer
            context['question'] = question
            return context


@login_required
def FollowFromAnswers(request, pk):
        user = get_object_or_404(User,pk=pk)
        friend,created = Friend.objects.get_or_create(current_user=request.user)
        friend.users.add(user)
        p1 = Profile.objects.get(user=user)
        p2 = Profile.objects.get(user=request.user)
        p2.following.add(user)
        p2.save()
        p1.followers.add(request.user)
        p1.save()
        return HttpResponse(request.path.info)

