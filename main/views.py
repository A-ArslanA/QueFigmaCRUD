from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.views.generic import DetailView, UpdateView, DeleteView


# DB Classes
class PostDetail(DetailView):
    model = Post
    template_name = 'post-details.html'
    context_object_name = 'postContext'


class EditPost(UpdateView):
    model = Post
    template_name = 'edit.html'
    # fields = ['name', 'content', 'little_content']
    form_class = PostForm


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = '/'

# USER FUNC


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {
        'posts': posts
    })


def add(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'add.html', {
        'form': form
    })

# def edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = PostForm(request.POST or None, instance=post)
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return redirect("post-details", pk=post.pk)
#     else:
#         form = PostForm()
#
#     return render(request, "user/edit.html", {
#         'post': post,
#         'form': form
#     })
