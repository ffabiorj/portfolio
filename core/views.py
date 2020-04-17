from django.shortcuts import render
from core.models import Project

def home(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, "blog/index.html", context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {'project': project}
    return render(request, "blog/project_detail.html", context)
