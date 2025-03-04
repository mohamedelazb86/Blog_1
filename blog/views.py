from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm

# CREATE CRUD OPERATION (LIST- DEATIL - CREATE - UPDATE- DELETE)
# CREATE CRUD BY FBV  AND CBV
def post_list(request):
    posts=Post.objects.all()
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.author=request.user
            myform.save()
            return redirect('/blog/')
    else:
        form=PostForm()
    context={
        'posts':posts,
        'form':form
    }
    return render(request,'blog/post_list.html',context)


def post_detail(request,pk):
    post=Post.objects.get(id=pk)
    context={
        'post':post
    }
    return render(request,'blog/post_detail.html',context)


def delete_post(request,id):
    post=Post.objects.get(id=id)
    post.delete()
    return redirect('/blog/')

def update_post(request,id):
    post=Post.objects.get(id=id)
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.author=request.user
            #myform.post=post

            myform.save()
            return redirect('/blog/')
    else:
        form=PostForm(instance=post)
    context={
        'form':form
    }
    return render(request,'blog/update_post.html',context)
    

