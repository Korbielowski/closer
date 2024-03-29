# Generated by Django 5.0.2 on 2024-03-17 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_alter_closeruser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='closeruser',
            name='about_me',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='closeruser',
            name='background_picture_url',
            field=models.ImageField(blank=True, upload_to='background_picture/'),
        ),
        migrations.AlterField(
            model_name='closeruser',
            name='current_city',
            field=models.CharField(blank=True, max_length=85),
        ),
        migrations.AlterField(
            model_name='closeruser',
            name='current_country',
            field=models.CharField(blank=True, max_length=28),
        ),
        migrations.AlterField(
            model_name='closeruser',
            name='current_state',
            field=models.CharField(blank=True, max_length=85),
        ),
        migrations.AlterField(
            model_name='closeruser',
            name='education',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='closeruser',
            name='gender',
            field=models.CharField(blank=True, choices=[('Unspecified', 'Unspecified'), ('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'), ('Helikopter szturmowy', 'Helikopter szturmowy')], max_length=20),
        ),
        migrations.AlterField(
            model_name='closeruser',
            name='home_city',
            field=models.CharField(blank=True, max_length=85),
        ),
        migrations.AlterField(
            model_name='closeruser',
            name='home_country',
            field=models.CharField(blank=True, max_length=28),
        ),
        migrations.AlterField(
            model_name='closeruser',
            name='home_state',
            field=models.CharField(blank=True, max_length=85),
        ),
        migrations.AlterField(
            model_name='closeruser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='closeruser',
            name='profile_picture_url',
            field=models.ImageField(blank=True, upload_to='profile_picture/'),
        ),
        migrations.AlterField(
            model_name='closeruser',
            name='relationship',
            field=models.CharField(blank=True, choices=[('Unspecified', 'Unspecified'), ('Single', 'Single'), ('Married', 'Married'), ('Engaged', 'Engaged'), ('Complicated', 'Complicated'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed'), ('Polyamorous', 'Polyamorous'), ('FWB', 'FWB')], max_length=20),
        ),
        migrations.AlterField(
            model_name='closeruser',
            name='religion',
            field=models.CharField(blank=True, choices=[('Unspecified', 'Unspecified'), ('Christianity', 'Christianity'), ('Islam', 'Islam'), ('Hinduism', 'Hinduism'), ('Buddhism', 'Buddhism'), ('Shinto', 'Shinto'), ('Taoism', 'Taoism'), ('Voodoo', 'Voodoo'), ('Folk religion', 'Folk religion'), ('Atheism', 'Atheism')], max_length=20),
        ),
        migrations.AlterField(
            model_name='closeruser',
            name='second_name',
            field=models.CharField(blank=True, max_length=70),
        ),
    ]
