from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def create_roles(sender, **kwargs):
    Group.objects.get_or_create(name='User')
    Group.objects.get_or_create(name='Manager')
    Group.objects.get_or_create(name='Admin')