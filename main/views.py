from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import EmailList, Item
from .forms import *
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import logout


# from django.conf import settings

# Create your views here.
# Page that sends emails
def send(response):
    if response.user.is_authenticated:
        # ls = EmailList.objects.all()
        ls = response.user.emaillist.all()
        if response.method == "POST":
            form = CreateNewList(response.POST)
            if form.is_valid():
                selectID = response.POST.get("group")
                emailInput = response.POST["email"]
                subject = response.POST["subject"]
                content = response.POST["content"]
                if selectID or emailInput:
                    if selectID != None:
                        list = EmailList.objects.get(id=selectID).item_set.all()
                        emails = [name.recipient for name in list]
                        # new = EmailList(item=selectID)
                        # new.save()
                    elif emailInput != "" and emailInput != None:
                        # list = EmailList.objects.get(name=emailInput).item_set.all()
                        emails = [emailInput]
                        # new = EmailList(name=emailInput)
                        # new.save()
                    send_mail(
                        subject,
                        content,
                        "settings.EMAIL_HOST_USER",
                        emails,
                        fail_silently=False,
                    )
                    messages.success(response, "Email was successfully sent.")
                    return HttpResponseRedirect(response.path_info)
                else:
                    messages.warning(response, "Please select a group or enter an email.")


                # form = CreateNewList()

        else:
            form = CreateNewList()
        return render(response, "main/send.html", {"form": form, "ls": ls})
    else:
        return render(response, "main/home.html", {})


# Page which displays the groups of emails
def recipientGroups(response):
    if response.user.is_authenticated:
        # ls = EmailList.objects.all()
        ls = response.user.emaillist.all()

        if response.method == "POST":
            for item in ls:
                # If the delete button was clicked
                if response.POST.get(str(item.id)) == "delete":
                    EmailList.objects.filter(id=item.id).delete()
                    return HttpResponseRedirect(response.path_info)
            # Create a new group
            if response.POST.get("newItem"):
                txt = response.POST.get("new")
                if len(txt) > 2:
                    new = EmailList(name=txt)
                    new.save()
                    response.user.emaillist.add(new)
                else:
                    print("invalid")
                return HttpResponseRedirect("/%i" % new.id)
        return render(response, "main/groups.html", {"ls": ls})
    else:
        return render(response, "main/home.html", {})


# Page which displays the emails inside groups
def recipients(response, id):
    if response.user.is_authenticated:
        ls = EmailList.objects.get(id=id)
        if ls in response.user.emaillist.all():
            if response.method == "POST":
                for item in ls.item_set.all():
                    # If the delete button was clicked
                    if response.POST.get(str(item.id)) == "delete":
                        ls.item_set.all().filter(id=item.id).delete()
                        return HttpResponseRedirect(response.path_info)
                # Add an email to the group
                if response.POST.get("newItem"):
                    txt = response.POST.get("new")
                    if len(txt) > 2:
                        ls.item_set.create(recipient=txt)
                        ls.save()
                    else:
                        print("invalid")
                    return HttpResponseRedirect(response.path_info)
                    # t = EmailList(name=n)
                    # t.save()
                    # response.user.todolist.add(t)
                    # return HttpResponseRedirect("/%i" % t.id)

            return render(response, "main/recipients.html", {"ls": ls})
    else:
        return render(response, "main/home.html", {})


def home(response):
    return render(response, "main/home.html", {})
def logout_view(response):
    logout(response)
    return redirect("/")