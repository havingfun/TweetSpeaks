from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from TweetSpeaks import settings
urlpatterns = [
    # Examples:
    url(r'^$', 'tweetsentiments.views.home', name='home'),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'^search/', 'tweetsentiments.views.home'),
    url(r'post_form.html','tweetsentiments.views.post_form', name='post_form'),
	url(r'^post_form_action.html$','tweetsentiments.views.home', name='post_form_upload'),
	# url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]