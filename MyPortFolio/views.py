from django.shortcuts import render

# Create your views here.


def HomeView(request):

    return render(request, "Home/home.html")

def ProjectView(request):
    return render(request, 'projects/projects.html')

def ResumeView(request):
    return render(request, 'resume/resume.html')

def ContactView(request):
    return render(request, 'contact/contact.html')