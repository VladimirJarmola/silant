from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from cars.models import Cars
from maintenance.models import Maintenance
from reclamation.models import Reclamation
from users.models import User


GROUPS = {
    'CL': 'CLIENT',
    'SE': 'SERVICE',
    'MG': 'MANAGER',
    'AD': 'ADMIN',
}

@receiver(post_save, sender=User)
def adding_to_group(sender: User, instance: User, **kwargs):
    '''
    При получении сигнал о сохранении юзера, добавляем его в группу.
    Если группы нет, то создаем ее.
    '''
    if instance.user_role == 'AD' and not instance.is_staff:
        instance.is_staff = True
        instance.save()
    if not instance.is_superuser:
        group, created = Group.objects.get_or_create(name=GROUPS[instance.user_role])
        transaction.on_commit(lambda: instance.groups.set([group], clear=True))


@receiver(post_save, sender=Group)
def adding_permision(sender: Group, instance: Group, **kwargs):
    '''
    При получении сигнала о сохранении группы назначаем ей права
    '''
    content_type_cars = ContentType.objects.get_for_model(Cars)
    content_type_maintenance = ContentType.objects.get_for_model(Maintenance)
    content_type_reclamation = ContentType.objects.get_for_model(Reclamation)
    content_type_users = ContentType.objects.get_for_model(User)

    cars_view_permission = Permission.objects.get(codename='view_cars', content_type=content_type_cars)
    cars_edit_permissions = list(Permission.objects.filter(content_type=content_type_cars).values_list('id', flat=True))

    maintenance_edit_permissions = Permission.objects.filter(content_type=content_type_maintenance).values_list('id', flat=True)

    reclamation_view_permission = Permission.objects.get(codename='view_reclamation', content_type=content_type_reclamation)
    reclamation_edit_permissions = Permission.objects.filter(content_type=content_type_reclamation).values_list('id', flat=True)

    deskbook_view_permission = Permission.objects.filter(content_type__app_label="deskbook", codename__startswith="view").values_list('id', flat=True)
    deskbook_edit_permissions = Permission.objects.filter(content_type__app_label="deskbook").values_list('id', flat=True)   

    user_view_permission = Permission.objects.get(codename='view_user', content_type=content_type_users)
    user_edit_permissions = Permission.objects.filter(content_type=content_type_users).values_list('id', flat=True)

    if instance.name == 'CLIENT':
        permissions_list = [cars_view_permission.id, reclamation_view_permission.id, user_view_permission.id] + list(maintenance_edit_permissions) + list(deskbook_view_permission)
    elif instance.name == 'SERVICE':
        permissions_list = [cars_view_permission.id, user_view_permission.id] + list(maintenance_edit_permissions) + list(reclamation_edit_permissions) + list(deskbook_view_permission)
    elif instance.name == 'MANAGER':
        permissions_list = [user_view_permission.id] + list(cars_edit_permissions) + list(maintenance_edit_permissions) + list(reclamation_edit_permissions) + list(deskbook_edit_permissions)
    elif instance.name == 'ADMIN':
        permissions_list = list(cars_edit_permissions) + list(maintenance_edit_permissions) + list(reclamation_edit_permissions) + list(deskbook_edit_permissions) + list(user_edit_permissions)
    
    transaction.on_commit(lambda: instance.permissions.set(permissions_list, clear=True))
