# Generated by Django 5.0.2 on 2024-05-27 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_remove_badges_badge_badges_new_user_badge_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badges',
            name='new_user_badge',
            field=models.CharField(choices=[('1', 'Newuser'), ('2', 'Poster'), ('3', 'Shorter'), ('4', 'Poller'), ('5', 'Tester')], default='1', max_length=20),
        ),
    ]
