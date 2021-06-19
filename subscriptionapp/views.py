from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscriptionapp.models import Subscribe


@method_decorator(login_required,'get')
class SubscribeView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail',kwargs={'pk':self.request.GET.get('project_pk')})

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project,pk=self.request.GET.get('project_pk'))
        user = self.request.user

        subscription = Subscribe.objects.filter(project=project,user=user)
        if subscription.exists():
            subscription.delete()
        else:
            Subscribe(user=user, project=project).save()
        return super(SubscribeView,self).get(self, request, *args, **kwargs)

class SubscribeListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    paginate_by = 5

    def get_queryset(self):
        projects = Subscribe.objects.filter(user=self.request.user).values_list('project')
        article_list = Article.objects.filter(project__in=projects)

        return article_list
