from django.db import migrations
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from app.models import Order  # Замените на правильный путь к вашей модели Order

def create_manager_group(apps, schema_editor):
    group, created = Group.objects.get_or_create(name='Менеджер')
    if created:
        content_type = ContentType.objects.get_for_model(Order)
        permissions = Permission.objects.filter(content_type=content_type)
        group.permissions.set(permissions)
        group.save()

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_order'),  # Замените на вашу последнюю миграцию
    ]

    operations = [
        migrations.RunPython(create_manager_group),
    ]
