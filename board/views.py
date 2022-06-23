from django.shortcuts import render

# Create your views here.
def list(request):
    return render(request, 'board/list.html')
#                          파일명


def view(request):
    return render(request, 'board/view.html')


def write(request):
    return render(request, 'board/write.html')