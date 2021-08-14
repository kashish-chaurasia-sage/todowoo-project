from django.forms.utils import to_current_timezone
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'todo/home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})
    else:

        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': "Username is already taken. Please choose a new username"})

        else:
            return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': "Password didn't match !"})


def currenttodos(request):
    todos = Todo.objects.filter(user=request.user, dateCompleted__isnull=True)
    completedtodos = Todo.objects.filter(
        user=request.user, dateCompleted__isnull=False).order_by('-dateCompleted')
    return render(request, 'todo/current.html', {'todos': todos, 'completedtodos': completedtodos})


@login_required
def completedtodos(request):
    completedtodos = Todo.objects.filter(
        user=request.user, dateCompleted__isnull=False)
    print("Completedtodos")
    print(completedtodos)
    return render(request, 'todo/completedtodos.html', {'todos': completedtodos})


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def signinuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signinuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todo/signinuser.html', {'form': AuthenticationForm(), 'error': 'Username and Password did not match !'})
        else:
            login(request, user)
            return redirect('currenttodos')


@login_required
def createtodo(request):
    if request.method == 'GET':
        return render(request, 'todo/createtodo.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/createtodo.html', {'form': AuthenticationForm(), 'error': 'BAD data passed'})


@login_required
def viewtodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'todo/viewtodo.html', {'todo': todo, 'form': form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('currenttodos')

        except ValueError:
            return render(request, 'todo/viewtodo.html', {'todo': todo, 'form': form, 'error': "BAD Info"})


@login_required
def completetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.dateCompleted = timezone.now()
        todo.save()
        return redirect('currenttodos')


@login_required
def deletetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        # todo.dateCompleted = timezone.now()
        todo.delete()
        return redirect('currenttodos')
