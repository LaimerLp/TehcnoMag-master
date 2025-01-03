# Generated by Django 4.2.16 on 2024-12-03 13:12

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_blogpost_image_alter_comment_id_alter_feedback_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
