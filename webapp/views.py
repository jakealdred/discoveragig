from django.shortcuts import render
from django.contrib.auth.models import User
from webapp.models import BandProfile, FanProfile, Achievement, Event, Comment
from webapp.forms import UserForm, BandProfileForm, FanProfileForm, EventForm, CommentForm
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
            registered = True

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
    
    context_dict['registered'] = registered
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

    if request.method == 'POST':
        comment_form = None
        try:
            comment_form = CommentForm(data=request.POST)
        except:
            pass

        if comment_form:
            comment = comment_form.save(commit=False)
            comment.event = event
            comment.user = request.user
            comment.save()

    if event:
        try:
            comments = Comment.objects.filter(event=event).order_by('date')
            context_dict['comments'] = comments
        except:
            pass
        rating = event.rating
        context_dict['event'] = event
        context_dict['rating'] = rating
    else:
        return HttpResponseRedirect('/create_event/')
    return render(request, 'webapp/event.html', context_dict)


def fan(request, username):
    context_dict = {}
    try:
        user = User.objects.get(username=username)
        profile = FanProfile.objects.get(user=user)
    except:
        profile = None

    if profile:
        context_dict['username'] = user.username
        context_dict['profile'] = profile
        if user == request.user:
            context_dict['logged_in'] = True
    else:
        return HttpResponseRedirect('/register/fan/')
    return render(request, 'webapp/fan.html', context_dict)


def band(request, username):
    context_dict = {}
    try:
        user = User.objects.get(username=username)
        profile = BandProfile.objects.get(user=user)
    except:
        profile = None

    if profile:
        context_dict['band'] = profile
        if user == request.user:
            context_dict['logged_in'] = True
    else:
        return HttpResponseRedirect('/register/band/')
    return render(request, 'webapp/band.html', context_dict)


@login_required
def create_event(request):
    context_dict = {}
    try:
        user = request.user
        band = BandProfile.objects.get(user=user)
    except:
        band = None

    if request.method != 'GET':
        if band:
            event_form = EventForm(data=request.POST)
            if event_form.is_valid():
                event = event_form.save(commit=False)
                event.band = band

                if 'picture' in request.FILES:
                    event.picture = request.FILES['picture']

                event.save()

                return HttpResponseRedirect('/event/%s' % event.slug)
    else:
        if band:
            event_form = EventForm()
            context_dict['event_form'] = event_form
        else:
            context_dict['error'] = 'Only bands can create new events.'

    return render(request, 'webapp/create_event.html', context_dict)


# Sends context info to all the templates
def get_context_info(request):

    context = {}
    user = request.user
    context['user'] = user
    try:
        fan = FanProfile.objects.get(user=user)
        context['fan_profile'] = fan
    except:
        pass
    try:
        band = BandProfile.objects.get(user=user)
        context['band_profile'] = band
    except:
        pass

    return context