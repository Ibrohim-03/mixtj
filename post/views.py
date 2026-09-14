from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

def posts(request):
    search_query = request.GET.get('search')
    if search_query:
        posts_list = Post.objects.filter(title__icontains=search_query)
    else:
        posts_list = Post.objects.all()

    return render(request, 'posts.html', {
        'posts': posts_list,
        'search_query': search_query or ''
    })

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        foto = request.FILES.get('foto')
        video = request.FILES.get('video')

        Post.objects.create(title=title, description=description, foto=foto, video=video)
        return redirect('posts')

    return render(request, 'create.html')

def edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.description = request.POST.get('description')
        
        if request.FILES.get('foto'):
            post.foto = request.FILES.get('foto')
        if request.FILES.get('video'):
            post.video = request.FILES.get('video')
            
        post.save()
        return redirect('posts')
        
    return render(request, 'edit.html', {'post': post})

def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('posts')
    return redirect('posts')
