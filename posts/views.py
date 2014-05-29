from django.template import RequestContext
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from posts.forms import PostForm

#Our model:
from posts.models import Post

def top_posts():
	latest_posts = Post.objects.all().order_by('-created_at')
	return latest_posts

@login_required
def index(request):
	posts = top_posts()
	context = RequestContext(request, {'posts': posts})
	return render_to_response('posts/index.html',
							  {'posts': posts,
							   'user': request.user
							   }, 
							  context_instance=RequestContext(request))#this is added to allow access to constants such as STATIC_URL.#


@login_required
def post(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)#creating the post but do not save yet to the database so we could set the user_posting just before we commit #
			post.user_posting = request.user
			post.save()
			return HttpResponseRedirect('/')#in case of successfull same go bak to the wall page with the new post in it#
	else:
		form = PostForm
		
	return render_to_response('posts/post.html',
							  {'form': form}, 
							  context_instance=RequestContext(request))

@login_required
def user_profile(request):
	user = request.user
	return render_to_response('posts/user_profile.html', 
		{'user': user}, 
		context_instance = RequestContext(request))