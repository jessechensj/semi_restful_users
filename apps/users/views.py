from django.shortcuts import render, HttpResponse, redirect
from models import User
from django.contrib import messages

# the index function is called when root is visited
def index(request):
  return render(request, 'index.html', {'users':User.objects.all()})

def new(request):
  return render(request, 'users_new.html')

def create(request):
  if request.method == "POST":
    if len(User.objects.validation(request.POST)) > 0:
      messages.error(request, User.objects.validation(request.POST))
      return redirect('/users/new')
    else:
      User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
      return redirect('/users')
  return redirect('/users/new')

def show(request, id):
  return render(request, 'users_show.html', {'user':User.objects.get(id=id)})

def edit(request, id):
  return render(request, 'users_edit.html', {'user':User.objects.get(id=id)})

def update(request, id):
  if request.method == "POST":
    if len(User.objects.validation(request.POST)) > 0:
      messages.error(request, User.objects.validation(request.POST))
      return redirect('/users/' + str(id) + '/edit')
    else:
      user = User.objects.get(id=id)
      user.first_name = request.POST['first_name']
      user.last_name = request.POST['last_name']
      user.email = request.POST['email']
      user.save()
      return redirect('/users/' + str(id)) 
  return redirect('/users/' + str(id))

def destroy(request, id):
  User.objects.get(id=id).delete()
  return redirect('/users')

# def clear(request):
#   User.objects.all().delete()
#   return redirect('/users')