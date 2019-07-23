import logging

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save, m2m_changed
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings


logger = logging.getLogger(__name__)


@receiver(m2m_changed, sender=get_user_model().groups.through)
def notify_user(sender, instance, action, model, pk_set, **kwargs):
    if action == 'post_add':
        groups = ', '.join([group.__str__() for group in model.objects.filter(pk__in=pk_set)])
        send_mail(
            f'You have been added to {groups}',
            f'An admin has added you to the following group/groups: {groups}. You are now granted all associated permissons.',
            settings.DEFAULT_FROM_EMAIL,
            [instance.email],
            fail_silently=False,
        )
        logger.debug(f'User {instance} added to {groups}. Email sent out.')

