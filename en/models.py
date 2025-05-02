from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import date

# Create your models here.
class ENProject(models.Model):
    
    CATEGORY_CHOICES = [
        ('RW', 'Real-world project'),
        ('PS', 'Personal project'),
        ('CH', 'Coding challenge'),
    ]

    title = models.CharField(_('title'), max_length=50)
    featured = models.BooleanField(_('featured'), default=False)
    date = models.DateField(_('date'), default=date.today)
    category = models.CharField(_('category'), max_length=2, choices=CATEGORY_CHOICES)
    stack = models.CharField(_('stack'), max_length=50)
    role = models.CharField(_('role'), max_length=100)
    info = models.TextField(_('info'), )
    image = models.ImageField(_('image'), null=True, blank=True, upload_to='projects')
    page_link = models.URLField(_('page_link'), null=True, blank=True,)
    github_link = models.URLField(_('github_link'), null=True, blank=True,)
    codepen_link = models.URLField(_('codepen_link'), null=True, blank=True,)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    modified_at = models.DateTimeField(_('modified_at'), auto_now=True)

    class Meta:
        db_table = 'en_projects'

    def __str__(self):
        return self.title