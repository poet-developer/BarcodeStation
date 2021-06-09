from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    class Mets:
        model = Article
        fields = ['title','image','content']