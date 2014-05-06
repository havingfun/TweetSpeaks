from django.shortcuts import render,RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from forms import KeyForm
from TwitterSentimentAnalysis.sentimentAnalyzer import *
	
# Create your views here.
#def home(request):
#    return render_to_response('index.html', locals(), context_instance = RequestContext(request))

def home(request):
	results = ""
	if request.method == 'GET':
		form = KeyForm()
	else:
		# A POST request: Handle Form Upload
		form = KeyForm(request.POST) # Bind data from request.POST into a PostForm
		# If data is valid, proceeds to create a new post and redirect the user
		if form.is_valid():
			keyword = form.cleaned_data['keyword']
			results = analyze(keyword)
	return render_to_response('index.html',{'form': form, 'results':results,},context_instance = RequestContext(request))