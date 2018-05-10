from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Paste
from .forms import PasteForm
from django.shortcuts import redirect

def index(request):
    if request.method == "POST":
        form = PasteForm(request.POST)
        if form.is_valid():
           form.save()
    else:
        form = PasteForm()

    ctx = {'form': form}
    return render(request, 'pastebin/index.jinja2', ctx)


def paste(request, id):
    paste = get_object_or_404(Paste, pk=id)
    ctx = {"paste": paste}
    return render(request, 'pastebin/paste-detail.jinja2', ctx)


def language_list(request, language):
    ctx = {'pastes': []}
    return render(request, 'pastebin/paste-language.jinja2', ctx)

def paste_new(request):
    if request.method == "POST":
        form = PasteForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PasteForm()
    return render(request, 'blog/post_edit.html', {'form': form})