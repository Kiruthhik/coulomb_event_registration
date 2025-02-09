from django.shortcuts import render,redirect
from .models import event,Participant,teammate
from django.contrib import messages
from .forms import ParticipantSignupForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def complete_profile(request):
    """ Ensures new users complete their profile after signing up with Google """
    user = request.user

    # Create a Participant profile if it doesn't exist
    if(Participant.objects.filter(user=user).exists()):
        messages.success(request, "Your profile is complete! You can now register for any event.")
        return redirect('/')  # Redirect to homepage if profile is already complete
    
    participant, created = Participant.objects.get_or_create(user=user)


    if request.method == 'POST':
        form = ParticipantSignupForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile is complete! You can now register for any event.")
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
    registered = False
    if request.user.is_authenticated:
        profile = Participant.objects.get(user=request.user)
        if profile in event_detail.participants.all():
            registered = True
    organizer = event_detail.organizers.all()
    context = {'event':event_detail,
               'registered':registered,
               'organizers':organizer}
    return render(request,'event.html',context)

@login_required
def profile(request):

    return render(request,'profile.html')

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
@login_required

def participant_register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        event_id = data.get("event_id")
        user = request.user

        if not user.is_authenticated:
            return JsonResponse({"status": "error", "message": "User not logged in"})

        event1 = event.objects.get(id=event_id)
        event1.participants.add(user.participant)

        return JsonResponse({"status": "success"})
    
    return JsonResponse({"status": "error", "message": "Invalid request"})
@csrf_exempt
@login_required
def teammate_register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        event_id = data.get("event_id")
        name = data.get("name")
        phone = data.get("phone")
        user = request.user

        if not user.is_authenticated:
            return JsonResponse({"status": "error", "message": "User not logged in"})

        event1 = event.objects.get(id=event_id)

        teammate1= teammate.objects.create(
            name=name, phone=phone, event=event1, team_of=user.participant
        )
        teammate1.save()
        # Create or update the participant
        # participant, created = Participant.objects.get_or_create(
        #     user=user, event=event,
        #     defaults={"name": name, "phone": phone}
        # )

        # if not created:
        #     participant.name = name
        #     participant.phone = phone
        #     participant.save()

        return JsonResponse({"status": "success"})
    
    return JsonResponse({"status": "error", "message": "Invalid request"})

@login_required
def profile(request):
    profile = Participant.objects.get(user=request.user)
    events = profile.events.all()
    teammates = profile.teammates.all()
    context = {
        'profile': profile,
        'events': events,
        'teammates': teammates
    }
    return render(request,'profile.html',context)