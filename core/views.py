from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactInquiry


def home(request):
    """Home page view."""
    return render(request, 'core/home.html')


def about(request):
    """About page view."""
    return render(request, 'core/about.html')


def products(request):
    """Products page view."""
    return render(request, 'core/products.html')


def contact(request):
    """Contact page view. Handles GET display and POST form submission."""
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and message:
            ContactInquiry.objects.create(
                name=name,
                email=email,
                message=message,
            )
            messages.success(
                request,
                'Thank you! Your message has been successfully submitted. We will get back to you soon.'
            )
            return redirect('contact')
        else:
            messages.error(request, 'Please fill in all fields before submitting.')

    return render(request, 'core/contact.html')
