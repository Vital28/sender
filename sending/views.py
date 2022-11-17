from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Client, Message, Sending
from .serializers import ClientSerializer, MessageSerializer, SendingSerializer


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()


class SendingViewSet(viewsets.ModelViewSet):
    serializer_class = SendingSerializer
    queryset = Sending.objects.all()

    @action(detail=True, methods=["get"])
    def info(self, request, pk=None):

        queryset_sending = Sending.objects.all()
        get_object_or_404(queryset_sending, pk=pk)
        queryset = Message.objects.filter(sending_id=pk).all()
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def fullinfo(self, request):

        total_count = Sending.objects.count()
        sending = Sending.objects.values("id")
        content = {
            "Total number of sending": total_count,
            "The number of messages sent": "",
        }
        result = {}

        for row in sending:
            res = {"Total messages": 0, "Sent": 0, "No sent": 0}
            mail = Message.objects.filter(sending_id=row["id"]).all()
            group_sent = mail.filter(sending_status="Sent").count()
            group_no_sent = mail.filter(sending_status="No sent").count()
            res["Total messages"] = len(mail)
            res["Sent"] = group_sent
            res["No sent"] = group_no_sent
            result[row["id"]] = res

        content["The number of messages sent"] = result
        return Response(content)
