# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def blog_index(request):
    # return HttpResponse("<h1>MY top blog</h1>")
    return render(request, "blog_index.html")

def article_01(request, numero_article):
    if numero_article in ["01", "02", "03"]:
        return render(request, f"Article_{numero_article}.html")
    return render(request, "Article_not_found.html")


# def article_02(request):
    #return render(request, "Article_02.html")

# def article_03(request):
    #return render(request, "Article_03.html")