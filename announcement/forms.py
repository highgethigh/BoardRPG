from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Post
from .models import Response

class PostForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ['title', 'text', 'category']


class RespondForm(forms.ModelForm):

    class Meta:
        model = Response
        fields = ('text', )

    def __init__(self, *args, **kwargs):
        super(RespondForm, self).__init__(*args, **kwargs)
        self.fields['text'].label = "Напишите свой отклик здесь"


class ResponsesFilterForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super(ResponsesFilterForm, self).__init__(*args, **kwargs)
        self.fields['title'] = forms.ModelChoiceField(
            label='Объявление',
            queryset=Post.objects.filter(author_id=user.id).order_by('-data').values_list('title', flat=True),
            empty_label="Все",
            required=False
        )

