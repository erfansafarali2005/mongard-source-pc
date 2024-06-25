from django.shortcuts import render , redirect
from .models import Todo
from django.contrib import messages
from .forms import TodoCreateForm , TodoUpdateForm

def home (request):

    all = Todo.objects.all() # all: sends all datas from model , first: first data , last : last data

    return render(request , "home.html" , {'todos' : all}) #every sent data to the frontend should be in dictionaries



def detail(request ,todo_id): #this todo_id comes from url 

    todo = Todo.objects.get(id=todo_id)

    return render(request , 'detail.html' , {'todo' : todo})

def delete (request , todo_id):
    try:
     Todo.objects.get(id=todo_id).delete()
     messages.success(request,'deleted successfully' , 'success')
    except:
        messages.error(request, 'there was an error' , 'danger')


    return redirect ("home")


def create(request):
 if request.method =="POST": # POST : he clicked on the submit button
     form = TodoCreateForm(request.POST)
     if form.is_valid():
         cd = form.cleaned_data # data coming from form
         Todo.objects.create(title= cd['title'] , body= cd['body'] , created=cd['created']) #
         #                     ^-> title from model           ^-> body from form
         messages.success(request , 'todo created successfully ' , 'success')
         return redirect('home')
 else: # Get : he recently came to the page and want to see the form
     form = TodoCreateForm
     return render(request , "create.html" , {"form" : form})



def update(request , todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method =="POST":
        form = TodoUpdateForm(request.POST , instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'model updated successfully' , 'success')
            return redirect('details' , todo_id)
    else: #Get

        form = TodoUpdateForm(instance=todo)

    return render(request , "update.html" , {"form": form})
