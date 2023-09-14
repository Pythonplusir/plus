from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from .models import Post
from django.utils.text import slugify


@receiver(pre_save, sender=Post)
def store_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title_slug)   