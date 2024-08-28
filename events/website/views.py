from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Compose the email
            email_subject = f"New Contact Form Submission: {subject}"
            email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            recipient_list = ['chrispinamary@gmail.com']
            
            try:
                # Send the email
                send_mail(email_subject, email_message, 'your_email@example.com', recipient_list)
            except BadHeaderError:
                return HttpResponseBadRequest('Invalid header found.')

            # Redirect or return a success response
            return HttpResponse('Your message has been sent. Thank you!')
    else:
        form = ContactForm()

    return render(request, 'your_template_name.html', {'form': form})

def index (request):
    return render (request, 'index.html')