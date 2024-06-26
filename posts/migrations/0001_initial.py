# Generated by Django 5.0.2 on 2024-05-20 11:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('title', models.CharField(default='', max_length=100)),
                ('question', models.CharField(max_length=500)),
                ('first_ans', models.CharField(max_length=500)),
                ('second_ans', models.CharField(max_length=500)),
                ('third_ans', models.CharField(max_length=500)),
                ('fourth_ans', models.CharField(max_length=500)),
                ('votes', models.IntegerField(default=0)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('title', models.CharField(default='', max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('image', models.ImageField(blank=True, upload_to='posts_images/')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('title', models.CharField(default='', max_length=100)),
                ('question', models.CharField(max_length=500)),
                ('first_ans', models.CharField(max_length=500)),
                ('second_ans', models.CharField(max_length=500)),
                ('third_ans', models.CharField(max_length=500)),
                ('fourth_ans', models.CharField(max_length=500)),
                ('correct_ans', models.CharField(max_length=500)),
                ('votes', models.IntegerField(default=0)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserPollAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=500)),
                ('answer_date', models.DateField(auto_now_add=True)),
                ('poll', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='poll', to='posts.poll')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='respondent', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserTestAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=500)),
                ('answer_date', models.DateField(auto_now_add=True)),
                ('test', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='posts.test')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
