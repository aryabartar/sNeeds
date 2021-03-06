from celery import shared_task, task

from django.utils import timezone

from sNeeds.apps.notifications.models import EmailNotification, SoldTimeSlotReminderEmailNotification, \
    SoldTimeSlotChangedEmailNotification
from sNeeds.utils.sendemail import send_sold_time_slot_start_reminder_email, send_sold_time_slot_changed_email


@shared_task
def send_email_notifications():
    qs = EmailNotification.objects.filter(
        send_date__lte=timezone.now(),
        sent=False
    )

    for obj in qs:
        # if obj.is_sold_time_slot_reminder():
        #     send_sold_time_slot_start_reminder_email(send_to=obj.email, **obj.get_data_dict())
        try:
            obj = obj.soldtimeslotreminderemailnotification
            send_sold_time_slot_start_reminder_email(send_to=obj.email, **obj.get_data_dict())
        except SoldTimeSlotReminderEmailNotification.DoesNotExist:
            pass

        try:
            obj = obj.soldtimeslotchangedemailnotification
            send_sold_time_slot_changed_email(send_to=obj.email, **obj.get_data_dict())
        except SoldTimeSlotChangedEmailNotification.DoesNotExist:
            pass

    qs.update(sent=True)
