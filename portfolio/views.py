from django.shortcuts import render, redirect
from .models import my_work
from portfolio.forms import contactformemail
from django.core.mail import send_mail
from django.contrib import messages

def index(request):
    works = my_work.objects.all()
    return render(request, "index.html", {'works': works})

def contactsendmail(request):
    if request.method == "POST":
        form = contactformemail(request.POST)
        if form.is_valid():
            fromemail = form.cleaned_data['fromemail']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            phone = form.cleaned_data['extra_field']

            # Send the email
            send_mail(
                subject,
                f"Message: {message}\nphone: {phone}",
                fromemail,
                ['tonykigsaka@gmail.com'], 
                fail_silently=False,
            )

            # Display a success message to the user
            messages.success(request, "Hello👋 I Have Received Your message, I Will Call You Soon!")

            # Redirect the user to a success page
            return redirect('index')
    else:
        form = contactformemail()
    
    works = my_work.objects.all()
    return render(request, 'index.html', {'form': form, 'works': works})
