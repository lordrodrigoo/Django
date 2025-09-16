from django.shortcuts import render
from . forms import RegisterForm

# Create your views here.

def register_view(request):
    if request.POST:
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()
    return render(request, 'author/pages/register_view.html', {
        'form': form,
    })