from django.shortcuts import render, get_object_or_404


from core.models import Post, Categories


def index(request):
    posts = Post.objects.all()

    return render(request, "core/index.html", {"posts": posts})


def categorie(request):
      categories = Categories.objects.all()

      context = {
          'categories': categories
      }
      return render(request, 'core/index.html', context)




# def show_post(request, post_slug):
#	post = get_object_or_404(Post, slug=post_slug)
#	data = {
##		'title' : post.title,
#'post' : post,
 #   }
#	return render(request, 'core/post.html', data)