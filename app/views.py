from pathlib import Path

from django.core.mail import send_mail
from django.shortcuts import redirect, render
import markdown

from app.forms import ContactForm
from config import settings_local


def index(request, page):
    pages = [
        "about",
        "start",
        "why",
        "comfort",
        "legs",
        "hands",
        "back",
        "chest",
        "shoulders",
        "head",
        "exercises",
        "sources",
        "contact",
    ]

    try:
        # check whether submitted page exists
        # in the above list of pages
        pages.index(page)

    except:
        return redirect("/")

    else:
        BASE_DIR = Path(__file__).resolve().parent.parent
        path = str(BASE_DIR) + "/templates/articles/" + page + ".mkd"
        mkd_file = open(path, "r", encoding="utf-8")
        mkd = mkd_file.read()
        html = markdown.markdown(mkd)

        context = {
            "page": page,
            "html": html,
        }

        return render(request, "article.html", context)


def contact(request):
    """Allow the user to send an email to the author."""

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            message = "From: " + email + "\n\n" + message

            send_mail(
                "MP - " + name + " " + subject,
                message,
                email,
                fail_silently=False,
            )
            context = {
                "page": "contact",
            }
            return render(request, "contact-success.html", context)

    else:
        form = ContactForm()

    context = {
        "page": "contact",
        "form": form,
    }

    return render(request, "contact.html", context)
