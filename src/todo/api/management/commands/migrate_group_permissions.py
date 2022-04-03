from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, **options):
        root_admin_g = Group.objects.create(name='root_admin')
        admin_g = Group.objects.create(name='admin')
        worker_g = Group.objects.create(name='worker')

        all_permissions = Permission.objects.all()
        root_admin_perms = all_permissions
        admin_perms = all_permissions.filter(content_type__model__in=
                                             ['task', 'project',
                                              'organization'])
        worker_perms = all_permissions.filter(codename__in=
                                              ['add_task', 'change_task',
                                               'view_task', 'view_project',
                                               'view_organization'])

        for p in root_admin_perms:
            root_admin_g.permissions.add(p)
        for p in admin_perms:
            admin_g.permissions.add(p)
        for p in worker_perms:
            worker_g.permissions.add(p)
