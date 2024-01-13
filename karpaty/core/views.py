from django.shortcuts import render


from core.models import Post


def index(request):
    posts = Post.objects.all()

    return render(request, "core/index.html", {"posts": posts})
