from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from blog.models import Post, Comments, Category, Feedback
from blog.forms import PostForm, CommentForm
from django.db.models import Avg

# Create your views here.
def post_list(request):
    posts = Post.objects.all().filter(published=True)
    category = Category.objects.all()
    counter_post = posts.count()
    context = {
        'items': posts,
        'category': category,
        'counter_post': counter_post
    }

    return render(request, 'blog/post_list.html', context)

def categories(request, category_pk):
    post = Post.objects.filter(category=category_pk)
    category = Category.objects.all()
    counter_post = post.count()
    return render(request, 'blog/post_list.html', {'items': post, 'category': category, 'counter_post': counter_post})


# добавить страничку с рекомендованными, где самые крутые посты
def recomends(request):
    posts = Post.objects.values('title', 'pk').annotate(Avg('feedbacks__rating')).order_by('-feedbacks__rating__avg')[:5]
    # posts = Post.objects.all().order_by('-rating')
    # posts = sorted(list(Post.objects.all()), key=lambda post: post.rating)
    # posts = Feedback.objects.filter(rating__gte=3).order_by('-rating')
    # feedback = set([i.post for i in posts])
    # posts = sorted(posts, key=posts.get)

    context = {
        'items': posts
    }
    return render(request, 'blog/post_feedbacks.html', context)


def post_draft(request):
    posts = Post.objects.all().filter(published=False)
    counter_post = posts.count()
    context = {'items': posts,'counter_post': counter_post}
    return render(request, 'blog/post_list.html', context)

def published_post(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.published = True
    post.save()
    return render(request, 'blog/post_detail.html', {'post': post})

def rating_feed(post_pk):
    fb = Feedback.objects.filter(post=post_pk)
    rating = 0
    if fb.count() != 0:
        rating = sum([i.rating for i in fb]) / fb.count()
    return round(rating, 1)

def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    rating = rating_feed(post_pk)
    comments = Comments.objects.filter(post=post_pk)
    # fb = Feedback.ob
    counter = comments.count()
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.publish_date = datetime.now()
            comment.save()
            return redirect('post_detail', post_pk=post.pk)
    else:
        comment_form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, "comments": comments,'counter': counter, 'comment_form': comment_form, 'rating': rating})


def post_new(request):
     if request.method == "GET":
        form = PostForm()
        return render(request, 'blog/post_new.html', {'form': form})
     else:
         form = PostForm(request.POST)
         if form.is_valid():
             post = form.save(commit=False)
             post.created_date = datetime.now()
             post.publish_date = datetime.now()
             post.save()
             return redirect('post_detail', post_pk=post.pk)

def post_edit(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == "GET":
        form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})
    else:
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = datetime.now()
            post.publish_date = datetime.now()
            post.save()
            return redirect('post_detail', post_pk=post.pk)
    
def post_delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk).delete()
    return redirect('post_list')


def feedback(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    fb = Feedback.objects.filter(post=post_pk)
    rating = rating_feed(post_pk)
    context = {'fb': fb,
               'post': post,
               'rating': rating,
               }
    return render(request, 'blog/feedback.html', context)


def MyPosts(request):
    posts = Post.objects.filter(author=request.user)
    context = {'items': posts,

               }
    return render(request, 'blog/post_my.html', context)









