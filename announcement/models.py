from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    CAT = (('tanks', 'Tanks'),
           ('healers', 'Healers'),
           ('damage_dealers', 'Damage Dealers'),
           ('dealers', 'Dealers'),
           ('gildmasters', 'Gildmasters'),
           ('quest_givers', 'Questgivers'),
           ('blacksmiths', 'Blacksmiths'),
           ('skiners', 'Skiners'),
           ('potion_makers', 'Potion makers'),
           ('spell_masters', 'Spell masters'))
    category = models.CharField(max_length=15, choices=CAT)
    data = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=256)
    text = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Response(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    status = models.BooleanField(default=False)
    data = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"{self.author.username} - {self.post.title} Отклик: {self.text}"