from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from.models import Post
from taggit.models import Tag


def post_list(request, tag_slug=None):
    object_list = Post.objects.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])    
    
    return render(request,
                 'blog/list.html',
                 {
                  'posts': object_list,
                  'tag': tag})


def post_detail(request, post):
    post = get_object_or_404(Post, slug=post) 

    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.objects.filter(tags__in=post_tags_ids)\
                                  .exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
                                .order_by('-same_tags','created_at')[:4]

    return render(request,
                  'blog/detail.html',
                  {'post': post,                   
                   'similar_posts': similar_posts})
