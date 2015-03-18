from django.shortcuts import render
from webapp.models import BandProfile, FanProfile, Achievement, Event, Comment
from webapp.forms import UserForm, BandProfileForm, FanProfileForm
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required

def index(request):

    context_dict = {}
    if request.method == 'POST':
        message = user_login(request)
        context_dict['message'] = message
    
    
    band_list = BandProfile.objects.order_by('-views')[:5]
    event_list = Event.objects.order_by('-views')[:5]
    context_dict['bands'] = band_list
    context_dict['events'] = event_list
    
    return render(request, 'webapp/index.html', context_dict)

def user_login(request):

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user:

        if user.is_active:
            login(request, user)
            return 'Success'
        else:
            return "Your Rango account is disabled."
    else:
        print "Invalid login details: {0}, {1}".format(username, password)
        return "Invalid login details supplied."


def register(request, user_type):

    registered = False
    context_dict = {}

    if request.method == 'POST':
        form = None
        user_form = UserForm(data=request.POST)
        if user_type == 'band':
            form = BandProfileForm(data=request.POST)
        elif user_type == 'fan':
            form = FanProfileForm(data=request.POST)
        
        if user_form.is_valid() and form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            # Auto login.
            user_login(request)
        else:
            print user_form.errors, form.errors

        return HttpResponseRedirect('/')
    else:
        user_form = UserForm()
        band_form = None
        fan_form = None
        if user_type == 'band':
            band_form = BandProfileForm()
            context_dict['band_form'] = band_form
        elif user_type == 'fan':
            fan_form = FanProfileForm()
            context_dict['fan_form'] = fan_form
    
    context_dict['user_form'] = user_form
    return render(request, 'webapp/register.html', context_dict)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def event(request, event_name):
    context_dict = {}
    try:
        event = Event.objects.get(slug=event_name)
    except:
        event = None

    if event:
        rating = event.rating
        context_dict['event'] = event
        context_dict['rating'] = rating
    else:
        return HttpResponseRedirect('/create_event/')
    return render(request, 'webapp/event.html', context_dict)