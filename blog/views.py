from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import Index, Comment, General, TableData
from .forms import CommentForm

class IndexView(generic.ListView):
    model = Index
    paginate_by = 4
    template_name = "blog/index.html"
    context_object_name = "contents"

class PostDetailView(generic.DetailView):
    model = Index
    template_name = "blog/post-detail.html"
    context_object_name = "details"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        return context


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        post = get_object_or_404(Index, id=int(self.kwargs["pk"]))
        obj.post = post
        messages.success(self.request, "Thank you for commenting our post!")
        return super().form_valid(form)

class CastsView(generic.ListView):
    model = General
    template_name = "blog/casts.html"
    context_object_name = "casts"

    def get_queryset(self):
        return super().get_queryset().filter(content_for="casts")

class SeasonsView(generic.ListView):
    model = General
    template_name = "blog/season.html"
    context_object_name = "seasons"

    def get_queryset(self):
        return super().get_queryset().filter(content_for="seasons")

    def get_context_data(self, **kwargs):
        context = super(SeasonsView, self).get_context_data(**kwargs)
        context["tables"] = TableData.objects.filter(content_for="seasons")
        return context

class AboutView(generic.ListView):
    model = General
    template_name = "blog/about.html"
    context_object_name = "abouts"

    def get_queryset(self):
        return super().get_queryset().filter(content_for="about")
