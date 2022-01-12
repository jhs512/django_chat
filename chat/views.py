from django.core.exceptions import ValidationError
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.core import serializers

# Create your views here.
from chat.models import ChatMessage


def room(request: HttpRequest):
    return render(request, "chat/chat_room.html", {})


def message_write(request: HttpRequest):
    writer = request.POST.get("writer", "")
    body = request.POST.get("body", "")

    if not writer:
        raise ValidationError("writer가 없습니다.")

    if not body:
        raise ValidationError("body가 없습니다.")

    ChatMessage(writer=writer, body=body).save()

    return JsonResponse({
        'message': "성공",
        'resultCode': "S-1"
    })


def messages(request: HttpRequest):
    id = request.GET.get('from_id')

    messages = list(ChatMessage.objects.filter(id__gt=id).order_by('id').values())

    return JsonResponse({
        'resultCode': "S-1",
        'messages': messages,
    })
