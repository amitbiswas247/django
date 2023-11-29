from django.shortcuts import render

posts = [
    {
        'author': 'AmitBiswas',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'July 24 , 2000'
    },
     {
        'author': 'AnjaliMishra',
        'title': 'Blog Post 2 ',
        'content': 'Second post content',
        'date_posted': 'September 21 , 2000'
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request ,'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})