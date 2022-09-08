from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import logging
# Create your views here.
def index(request):
    logger = logging.getLogger(__name__)


    logger.info("Simple info")
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
