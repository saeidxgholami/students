from django.shortcuts import render

from .models import Post, Person


def home(requeset):
	posts = Post.objects.all()
	return render(requeset, 'blog/index.html', {'posts': posts, 'user': 'John Doe'})


def save_person(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		age = request.POST.get('age')
		# create a person object to save in db
		Person.objects.create(name=name, age=age)
		print(f'{name} with {age} saved.')

	return render(request, 'blog/person.html')