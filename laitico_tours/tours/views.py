from django.shortcuts import render, get_object_or_404, redirect
from .models import Destination
from .forms import InquiryForm, BookingForm, TailorPackageForm
from django.contrib import messages
from django.http import JsonResponse

def home(request):
    destinations = Destination.objects.all()
    return render(request, 'home.html', {'destinations': destinations})

def destinations(request):
    destinations = Destination.objects.all()
    return render(request, 'destinations.html', {'destinations': destinations})

def destination_detail(request, slug):
    destination = get_object_or_404(Destination, slug=slug)
    return render(request, 'destination_detail.html', {'destination': destination})

def book_tour(request, slug):
    destination = get_object_or_404(Destination, slug=slug)
    success = False  

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.destination = destination 
            booking.save()
            success = True
    else:
        form = BookingForm(initial={'destination': destination})

    return render(request, 'booking_form.html', {'form': form, 'destination': destination, 'success': success})


def about(request):
    return render(request, 'about.html' )

def contact(request):
    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
    else:
        form = InquiryForm()

    return render(request, 'contact.html', {'form': form})

def tailoredPackages(request):
    if request.method == "POST":
        form = TailorPackageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your tailored package has been sent successfully!")
            return redirect('packages')
    else:
        form = TailorPackageForm()
    return render(request, 'tailored-package.html', {'form': form} )