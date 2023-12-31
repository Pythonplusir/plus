# Generated by Django 4.2.3 on 2023-09-14 07:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True, verbose_name='email')),
                ('full_name', models.CharField(blank=True, max_length=191)),
                ('short_name', models.CharField(blank=True, max_length=191)),
                ('photo', models.ImageField(blank=True, default='images/assets/default_image.jpg', upload_to='images/')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('django_course', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('course_type', models.CharField(blank=True, choices=[('FREE', 'FREE'), ('PAID', 'PAID')], default='PAID', max_length=4)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_date', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('authority', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_word', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=0, max_digits=10)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('failed', 'Failed'), ('completed', 'Completed')], default='pending', max_length=10)),
                ('invoice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accountsApp.invoice')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, unique=True, verbose_name='عنوان سوال')),
                ('body', models.TextField(verbose_name='متن  سوال')),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('views', models.IntegerField(default=0)),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, to='accountsApp.tags')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, verbose_name='نام و نام خانوادگی')),
                ('phone', models.CharField(max_length=11, verbose_name='شماره همراه')),
                ('is_apply', models.BooleanField(default=False)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('order_date', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('paid', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-order_date',),
            },
        ),
        migrations.AddField(
            model_name='invoice',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accountsApp.order'),
        ),
    ]
