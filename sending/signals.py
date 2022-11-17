from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Client, Message, Sending
from .tasks import send_message


@receiver(post_save, sender=Sending, dispatch_uid="create_message")
def create_message(sender, instance, created, **kwargs):
    if created:
        sending = Sending.objects.filter(id=instance.id).first()
        clients = Client.objects.filter(
            Q(mobile_operator_code=sending.mobile_operator_code) | Q(tag=sending.tag)
        ).all()

        for client in clients:
            Message.objects.create(
                sending_status="No sent", client_id=client.id, mailing_id=instance.id
            )
            message = Message.objects.filter(
                mailing_id=instance.id, client_id=client.id
            ).first()
            data = {
                "id": message.id,
                "phone": client.phone_number,
                "text": sending.text,
            }
            client_id = client.id
            sending_id = sending.id

            if instance.to_send:
                send_message.apply_async(
                    (data, client_id, sending_id), expires=sending.date_end
                )
            else:
                send_message.apply_async(
                    (data, client_id, sending_id),
                    eta=sending.date_start,
                    expires=sending.date_end,
                )
