from django.shortcuts import render

# Create your views here.
def home(request):
    """
    return views at / url
    """
    return render(request, "home.html", {})
    