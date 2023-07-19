from django.urls import path
from blog.views import *
urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/draft/', post_draft, name='post_draft'),
    path('post/detail/<int:post_pk>', post_detail, name='post_detail'),
    path('post/published/<int:post_pk>', published_post, name='published_post'),
    path('post/category/<int:category_pk>', categories, name='categories'),
    path('post/edit/<int:post_pk>', post_edit, name='post_edit'),
    path('post/delete/<int:post_pk>', post_delete, name='post_delete'),
    path('post/new/', post_new, name='post_new'),
    path('post/detail/feedback/<int:post_pk>', feedback, name='feedback'),
    path('post/recomendations/', recomends, name='recomends'),
    path('post/MyPosts', MyPosts, name='MyPosts'),

]