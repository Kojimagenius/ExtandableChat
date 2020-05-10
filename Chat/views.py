from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
import json


def index(request):
    return render(request, 'Chat/index.html', {})


@login_required
def room(request, room_name):
    return render(request, "Chat/room.html", {
        'room_name': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username))
    })

# Create your views here.
