from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import Student
from django.core.mail import send_mail
from django.conf import settings


def home(request):
 return render(request, 'index.html')

def RegisterUser(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if email already exists
        if Student.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'index.html', {
                'full_name': full_name,
                'email': email,
                'phone_number': phone_number,
            })
        
        # Check if passwords match
        if password == confirm_password:
            # Create and save student with hashed password
            student = Student.objects.create(
                full_name=full_name,
                email=email,
                phone_number=phone_number,
                password=make_password(password)
            )
            student.save()

              # Send confirmation email
            send_mail(
                subject='Registration Successful - Zero2Code Bootcamp',
                message=f'Dear {full_name},\n\nThank you for registering for the Zero2Code Bootcamp! We look forward to seeing you in class.\n\nBest regards,\nZero2Code Team',
                from_email=None,  # Uses DEFAULT_FROM_EMAIL if None
                recipient_list=[email],
                fail_silently=False,
                )

        # try:
        #        send_mail(
        #        'Test Subject',
        #        'This is a test email.',
        #        settings.DEFAULT_FROM_EMAIL,
        #        ['recipient@example.com'],
        #        fail_silently=False,
        #        )
        #        print("Email sent successfully!")
        # except Exception as e:
        #        print(f"Failed to send email: {e}")

        # return render(request, 'success.html')
    else:
            messages.error(request, 'Passwords do not match. Try again.')
            return render(request, 'index.html', {
                'full_name': full_name,
                'email': email,
                'phone_number': phone_number,
            })

    return render(request, 'index.html')

def SuccessPage(request):
 return render(request, 'success.html')
