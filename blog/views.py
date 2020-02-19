from django.shortcuts import render

# Create your views here.
#start inputs: Tuj
from blog.models import Post

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)
#end inputs: Tuj
