from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('tweets.views',

    url(r'^$', 
        'recent_tweets', 
        name='tweets-recent_tweets'),

    url(r'^add/$',
        'add_tweet', 
        name='tweets-add_tweet'),
    
    url(r'^(?P<username>.*)/$', 
        'user_tweets', 
        name='tweets-user_tweets'),
)

