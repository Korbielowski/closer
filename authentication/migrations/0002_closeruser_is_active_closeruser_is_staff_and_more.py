# Generated by Django 5.0.2 on 2024-03-12 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='closeruser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='closeruser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='closeruser',
            name='gender',
            field=models.CharField(choices=[('Unspecified', 'Unspecified'), ('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'), ('Helikopter szturmowy', 'Helikopter szturmowy')], max_length=20),
        ),
        migrations.AlterField(
            model_name='closeruser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='closeruser',
            name='relationship',
            field=models.CharField(choices=[('Unspecified', 'Unspecified'), ('Single', 'Single'), ('Married', 'Married'), ('Engaged', 'Engaged'), ('Complicated', 'Complicated'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed'), ('Polyamorous', 'Polyamorous'), ('FWB', 'FWB')], max_length=20),
        ),
        migrations.AlterField(
            model_name='closeruser',
            name='religion',
            field=models.CharField(choices=[('Unspecified', 'Unspecified'), ('Christianity', 'Christianity'), ('Islam', 'Islam'), ('Hinduism', 'Hinduism'), ('Buddhism', 'Buddhism'), ('Shinto', 'Shinto'), ('Taoism', 'Taoism'), ('Voodoo', 'Voodoo'), ('Folk religion', 'Folk religion'), ('Atheism', 'Atheism')], max_length=20),
        ),
    ]
