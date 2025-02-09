from django.forms import ModelForm, ValidationError

from .views import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')

    def clean_text(self):
        data = self.cleaned_data['text']
        if data == '':
            raise ValidationError('А кто поле будет заполнять, Пушкин?')
        return data
