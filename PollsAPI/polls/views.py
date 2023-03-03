from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

import rich
from rich.text import Text
from rich.panel import Panel 

from .models import Poll

def polls_list(request):
    MAX_OBJECT = 20 
    polls = Poll.objects.all()[:MAX_OBJECT]
    
    for poll in polls: 
        rich.print(
            Panel.fit(
                f"{poll.question}, {poll.created_by}, {poll.pub_date}",
                style='red'
            ),
            end="\t"
        )

    data = {
        "results": list(polls.values("question", "created_by__username", "pub_date"))
    }
    return JsonResponse(data)

def polls_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {
        "result": dict(
            question=poll.question,
            created_by=poll.created_by.username,
            pub_date=poll.pub_date
        )
    }
    for k in data:
        rich.print(
            Panel.fit(
                f"{k}, {data[k]}",
                style="cyan"
            ),
        )
    return JsonResponse(data)

