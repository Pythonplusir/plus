# Generated by Django 4.2.3 on 2023-09-14 09:23

from django.db import migrations, models
import django_jalali.db.models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='مهدی آزادی', max_length=30)),
                ('title', models.CharField(max_length=100, verbose_name='تگ عنوان اصلی')),
                ('title_tag', models.CharField(max_length=100, verbose_name='تگ-seo')),
                ('meta_desc', models.CharField(max_length=100, verbose_name='متا-تگ')),
                ('title_slug', models.CharField(blank=True, max_length=100, verbose_name='تگ-slug')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='اسلاگ')),
                ('img_banner', models.ImageField(default='blog_image.jpg', upload_to='images/', verbose_name='تصویر بنر')),
                ('img_small_one', models.ImageField(upload_to='images/')),
                ('title_one', models.CharField(max_length=100)),
                ('text_one', models.TextField()),
                ('title_two', models.CharField(max_length=100)),
                ('text_two', models.TextField()),
                ('title_tree', models.CharField(max_length=100)),
                ('text_tree', models.TextField(blank=True)),
                ('text_four', models.TextField(blank=True)),
                ('text_five', models.TextField(blank=True)),
                ('text_sex', models.TextField(blank=True)),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('views', models.IntegerField(default=0, editable=False)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]