from django.shortcuts import render

# Create your views here.
def list(request):
    return render(request, 'board/list.html')
#                          파일명


def views(request):
    return render(request, 'board/views.html')


def write(request):
    return render(request, 'board/write.html')