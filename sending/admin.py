from django.contrib import admin

from .models import Client, Message, Sending

admin.site.register(Sending)
admin.site.register(Client)
admin.site.register(Message)
