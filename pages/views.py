from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Team
from cars.models import Car
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your views here.

def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by("-created_date").filter(is_featured=True)
    all_cars = Car.objects.order_by("-created_date")
    # search_fields = Car.objects.values("model","city","year","body_style")
    model_search = Car.objects.values_list("model", flat=True).distinct()
    city_search = Car.objects.values_list("city", flat=True).distinct()
    year_search = Car.objects.values_list("year", flat=True).distinct()
    style_search = Car.objects.values_list("body_style", flat=True).distinct()

    data = {
        "teams": teams,
        "all_cars": all_cars,
        "featured_cars": featured_cars,
        "model_fields": model_search,
        "city_fields": city_search,
        "year_fields": year_search,
        "style_fields": style_search
    }
    return render(request, "pages/home.html", data)

def about(request):
    teams = Team.objects.all()
    data = {
        "teams": teams
    }
    return render(request, "pages/about.html", data)

def services(request):
    return render(request, "pages/services.html")

def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        message_body = f"Name: {name}     Email: {email}    Phone: {phone}    Message:{message}"

        
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
                f"You have a new message regarding {subject}",
                message_body,
                'rasulmuhamedovabduqayum@gmail.com',
                [admin_email],
                fail_silently=False,
            )
        messages.success(request, "Thank you for contacting us. We will get back to you shortly")
        return redirect("contact")

    return render(request, "pages/contact.html")