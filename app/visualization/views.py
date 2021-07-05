from django.shortcuts import render


def vis(request):
    return render(request, 'visualization.html')
