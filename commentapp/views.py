from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, DeleteView

from articleapp.models import Article
from commentapp.decorators import comment_ownership_required
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment

has_ownshin =[login_required,comment_ownership_required]

@method_decorator(login_required,'get')
@method_decorator(login_required,'post')

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        temp_data = form.save(commit=False)
        temp_data.article = Article.objects.get(pk=self.request.POST['article_pk'])
        temp_data.writer = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail',kwargs={'pk':self.object.article.pk})


class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'

    def get_success_url(self):
        return reverse('articleapp:detail',kwargs={'pk':self.object.article.pk})