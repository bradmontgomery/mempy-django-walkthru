from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from models import Tweet
from forms import TweetForm

def recent_tweets(request):
    recent_tweets = Tweet.objects.all()

    template_data = {
        'recent_tweets': recent_tweets[:10],
    }
    template = "tweets/recent_tweets.html"
    ctx = RequestContext(request)

    return render_to_response(
        template, 
        template_data, 
        context_instance=ctx
    )

@login_required
def add_tweet(request):

    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.posted_by = request.user
            tweet.save()
            url = reverse("tweets-user_tweets", args=[request.user])
            return redirect(url)
    else:
        form = TweetForm()
    
    template_data = {
        "form": form,
    }
    template = "tweets/add_tweet.html"
    ctx = RequestContext(request)

    return render_to_response(
        template, 
        template_data, 
        context_instance=ctx
    )

def user_tweets(request, username):
    tweets = Tweet.objects.filter(posted_by__username=username)

    template_data = {
        'tweets': tweets[:10],
        'username': username,
    }
    template = "tweets/user_tweets.html"
    ctx = RequestContext(request)

    return render_to_response(
        template, 
        template_data, 
        context_instance=ctx
    )

