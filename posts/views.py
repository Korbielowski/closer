from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q

from .forms import PostForm, PollFrom, TestFrom
from .models import Poll, UserPollAnswer, Test, UserTestAnswer


def create_post(request) -> HttpResponse:
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("profile", request.user.user_id)
    content = {"post_form": PostForm()}
    return render(request, "posts/post_creation.html", content)


def create_poll(request) -> HttpResponse:
    if request.method == "POST":
        poll_form = PollFrom(request.POST)
        if poll_form.is_valid():
            poll = poll_form.save(commit=False)
            poll.author = request.user
            poll.save()
            return redirect("profile", request.user.user_id)
    content = {"poll_form": PollFrom()}
    return render(request, "posts/poll_creation.html", content)


def poll_answer(request, poll_id, answer) -> HttpResponse:
    poll = Poll.objects.get(id=poll_id)
    if UserPollAnswer.objects.filter(
        Q(poll=poll) & Q(user=request.user.user_id)
    ).count():
        print("Cannot fill the poll twice")
        return redirect("profile", request.user.user_id)

    poll.votes += 1
    poll.save()

    poll_ans = UserPollAnswer()
    poll_ans.poll = poll
    poll_ans.answer = answer
    poll_ans.user = request.user
    poll_ans.save()

    return redirect("profile", request.user.user_id)


# TODO: create tests
def create_test(request) -> HttpResponse:
    if request.method == "POST":
        test_form = TestFrom(request.POST)
        if test_form.is_valid():
            test = test_form.save(commit=False)
            test.author = request.user
            test.save()
            return redirect("profile", request.user.user_id)
    content = {"test_form": TestFrom()}
    return render(request, "posts/test_creation.html", content)


def test_answer(request, test_id, answer) -> HttpResponse:
    test = Test.objects.get(id=test_id)
    if UserTestAnswer.objects.filter(
        Q(test=test) & Q(user=request.user.user_id)
    ).count():
        print("Cannot fill the test twice")
        return redirect("profile", request.user.user_id)

    test.votes += 1
    test.save()

    test_ans = UserTestAnswer()
    test_ans.test = test
    test_ans.answer = answer
    test_ans.user = request.user
    test_ans.save()

    if Test.objects.filter(Q(id=test_id) & Q(correct_ans=answer)).count():
        print("Well done, your answer is correct")

    return redirect("profile", request.user.user_id)
