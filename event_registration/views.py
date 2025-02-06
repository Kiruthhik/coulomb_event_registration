from django.shortcuts import render,redirect
from .models import event,Participant
from .forms import ParticipantSignupForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def complete_profile(request):
    """ Ensures new users complete their profile after signing up with Google """
    user = request.user

    # Create a Participant profile if it doesn't exist
    participant, created = Participant.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = ParticipantSignupForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to homepage after completion
    else:
        form = ParticipantSignupForm(instance=participant)

    return render(request, 'profile_edit.html', {'form': form})

def home(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')

def events(request):
    events = event.objects.all()
    context = {'events':events}
    return render(request,'events.html',context)

def event_detail(request,id):
    event_detail = event.objects.get(id=id)
    context = {'event':event_detail}
    return render(request,'event.html',context)