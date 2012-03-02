from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.views.decorators.cache import cache_page
from django.template import RequestContext
from main.models import Zombie, Tweet
from main.forms import ZombieForm, TweetForm

@cache_page(60 * 15)
def home(request):
	zombie= Zombie.objects.all()
	return render_to_response('home.html',{
		'zombie':zombie
	})

@cache_page(60 * 15)
def show_zombie(request, pk):
	zombie = get_object_or_404(Zombie, pk=pk)
	return render_to_response('show_zombie.html', {
		'zombie':zombie,
		})

def add_zombie(request):
		form = ZombieForm()
		if request.method == 'POST' :
				form = ZombieForm(request.POST)
				if form.is_valid():
					form.save()
					return redirect('home')
		return render_to_response('add_zombie.html',{
		'form': form,
		},RequestContext(request))

def edit_zombie(request,pk):
	zombie = get_object_or_404(Zombie, pk=pk)
	form = ZombieForm(instance=zombie)
	if request.method == 'POST':
		form = ZombieForm(request.POST, instance=zombie)
		if form.is_valid():
			form.save()
			return redirect('home')
	return render_to_response('add_zombie.html',{
		'form': form,
		},RequestContext(request))

def delete_zombie(request,pk):
	Zombie.objects.filter(pk=pk).delete()
	return redirect('home')