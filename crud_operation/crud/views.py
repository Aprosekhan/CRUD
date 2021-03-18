from django.shortcuts import render,HttpResponseRedirect

from .form import RegisterForm

from .models import Post

def show_data(request):
    if request.method == "POST":
        fm = RegisterForm(request.POST)
        if fm.is_valid():
            Nm = fm.cleaned_data['Name']
            Em = fm.cleaned_data['Email']
            Pw = fm.cleaned_data['Password']
            reg = Post(Name=Nm, Email=Em, Password=Pw)
            reg.save()
            fm = RegisterForm()
            
    else:
        fm = RegisterForm()
    stud = Post.objects.all()
    return render(request , "crud/register.html",{'form':fm, 'stu':stud})


def update_data(request,id):
    if request.method == 'POST':
        pi = Post.objects.get(pk=id)
        form = RegisterForm(request.POST,instance=pi)
        if form.is_valid():
            form.save()
    else:
        pi = Post.objects.get(pk=id) 
        form = RegisterForm(instance=pi)
    return render(request, 'crud/update.html', {'form':form})
        


def delete_data(request, id):
    if request.method == 'POST':
        pi = Post.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')



