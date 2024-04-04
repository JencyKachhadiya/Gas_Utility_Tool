from django.db.models import Case, When
from django.utils import timezone
from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from .models import ServiceRequest
from django.db import models
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES, initial={'customer_name': request.user.username, 'email': request.user.email})
        if form.is_valid():
            instance = form.save(commit=False)
            instance.customer_name = request.user.username
            instance.email = request.user.email
            instance.save()
            request.session['submit_request_completed'] = True
            return redirect('request_tracking')
    else:
        form = ServiceRequestForm(initial={'customer_name': request.user.username, 'email': request.user.email})
    return render(request, 'submit_request.html', {'form': form})

@login_required
def track_requests(request):
    user_requests = ServiceRequest.objects.filter(customer_name=request.user.username)
    return render(request, 'request_tracking.html', {'requests': user_requests})