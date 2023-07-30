from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import EmailList, Item
# from .forms import CreateNewList, email, subject, content
from .forms import *
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(response, id):
    ls = EmailList.objects.get(id=id)
    return render(response, "main/list.html", {"ls": ls})
def send(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            to = response.POST["email"]
            subject = response.POST["subject"]
            content = response.POST["content"]
            send_mail(
                subject,
                content,
                "settings.EMAIL_HOST_USER",
                [to],
                fail_silently=False,
            )
            form = CreateNewList()
            # t = EmailList(name=n)
            # t.save()
            # response.user.todolist.add(t)
            # return HttpResponseRedirect("/%i" % t.id)

    else:
        form = CreateNewList()
    return render(response, "main/send.html", {"form": form})
def home(response):
    return render(response, "main/base.html", {})