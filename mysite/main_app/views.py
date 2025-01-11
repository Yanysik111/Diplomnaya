from django.shortcuts import render, redirect
from .models import Text
from .forms import TextForm

def index(request):
    texts = Text.objects.all().order_by('-id')
    form = TextForm()
    context = {'texts': texts, 'form': form}
    return render(request, 'main_app/index.html', context)

def save_text(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return redirect('index')