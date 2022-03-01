# Generated by Django 3.2.9 on 2021-12-10 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_auto_20211210_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='nameqaz',
        ),
        migrations.RemoveField(
            model_name='post',
            name='postCategory',
        ),
        migrations.RemoveField(
            model_name='post',
            name='titleqaz',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='newapp.category'),
        ),
    ]