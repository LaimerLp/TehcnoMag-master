# Generated by Django 4.2.16 on 2024-11-30 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name': 'Обратная связь', 'verbose_name_plural': 'Обратная связь'},
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='age',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='satisfaction',
        ),
        migrations.AddField(
            model_name='feedback',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='Оценка сайта'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='suggestions',
            field=models.TextField(blank=True, null=True, verbose_name='Предложения'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='comments',
            field=models.TextField(verbose_name='Комментарии'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='subscribe',
            field=models.BooleanField(default=False, verbose_name='Подписаться на новости'),
        ),
    ]