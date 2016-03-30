from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'the_blah.html')

def blog(request):
	return  render(request, 'blog.html')

