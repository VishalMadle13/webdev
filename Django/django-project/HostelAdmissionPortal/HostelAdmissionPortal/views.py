from django.http import HttpResponse

def loginPage(request):
    return HttpResponse("This is login page")