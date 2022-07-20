from django.shortcuts import render, redirect
from django.contrib import messages

## import todo form and models

from .forms import StudyBlogForm
from .models import StudyBlog

###############################################

def index(request):

	item_list = StudyBlog.objects.order_by("-date")
	if request.method == "POST":
		form = StudyBlogForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('studyblog')
	form = StudyBlogForm()

	page = {
			"forms" : form,
			"list" : item_list,
			"title" : "TOPIC YOU STUDIED",
		}
	return render(request, 'studyblog/index.html', page)


def remove(request, item_id):
	item = StudyBlog.objects.get(id=item_id)
	item.delete()
	messages.info(request, "item removed !!!")
	return redirect('studyblog')
