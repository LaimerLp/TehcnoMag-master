# assign_manager.py
from django.contrib.auth.models import User, Group

def assign_manager_role(username):
    try:
        user = User.objects.get(username=username)
        manager_group, created = Group.objects.get_or_create(name='Менеджер')
        user.groups.add(manager_group)
        user.save()
        print(f"User {username} has been assigned to the 'Менеджер' group.")
    except User.DoesNotExist:
        print(f"User {username} does not exist.")

if __name__ == "__main__":
    import django
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")
    django.setup()

    # Замените 'your_username' на имя пользователя, которого вы хотите назначить в группу "Менеджер"
    assign_manager_role('manager')

