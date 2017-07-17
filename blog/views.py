import datetime
from django.db.models import Q
from django.shortcuts import render
from .models import Post


def post_list(request):
    qs = Post.objects.all()

    query = request.GET.get('query', '')
    if query:
        condition = Q(title__icontains=query) | Q(content__icontains=query)
        qs = qs.filter(condition)

    date_list = []
    for i in range(365):
        date = datetime.datetime(2017, 1, 1) + datetime.timedelta(days=i)
        date_list.append(date)

    return render(request, 'blog/post_list.html', {
        'post_list': qs,
        'query': query,
        'date_list': date_list,
    })


def post_detail(request, pk):
    # pk = "100"  # /blog/100/
    # post = Post.objects.get(id=pk)
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post': post,
    })

