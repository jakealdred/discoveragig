from django.shortcuts import render
from django.contrib.auth.models import User
from webapp.models import UserProfile, BandProfile, FanProfile, Achievement, Event, Comment, Feedback
from webapp.forms import UserForm, UserProfileForm, FanProfileForm, BandProfileForm, EventForm, CommentForm, FeedbackForm
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from webapp.data_choices import CITIES, GENRES

from django.utils import timezone

visits = {}

def index(request):

    context_dict = {}
    if request.method == 'POST':
        message = user_login(request)
        context_dict['message'] = message
    
    upcoming_list = Event.objects.order_by('date')[:5]
    #band_list = BandProfile.objects.order_by('-views')[:5]
    event_list = Event.objects.order_by('-views')[:5]
    #context_dict['bands'] = band_list



    context_dict['events'] = event_list
    context_dict['upcoming'] = upcoming_list 

    try:
        profile = UserProfile.objects.get(user=request.user)
        band = BandProfile.objects.get(profile=profile)
    except:
        band = None

    try:
        recommended_events = Event.objects.filter(genre = profile.genre)[:5]
    except:
        pass

    try:
        context_dict['recommended'] = recommended_events
    except:
        pass

    if band:
        try:
            feedback = Feedback.objects.filter(band=band).order_by('date')
            context_dict['feedback'] = feedback
        except:
            feedback = None

        if feedback:
            even = []
            odd = []
            i = 0
            for fb in feedback:
                if i%2==1:
                    odd += [fb]
                else:
                    even += [fb]
                i += 1


            context_dict['even'] = even
            context_dict['odd'] = odd

    return render(request, 'webapp/index.html', context_dict)

def user_login(request):

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user:
        login(request, user)
    else:
        print "Invalid login details: {0}, {1}".format(username, password)
        return "Invalid login details supplied."


def register(request, user_type):

    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

    context_dict = {}

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_profile_form = UserProfileForm(data=request.POST)
        
        if user_form.is_valid() and user_profile_form.is_valid():
            # User
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            # UserProfile
            user_profile = user_profile_form.save(commit=False)
            user_profile.user = user
            if 'picture' in request.FILES:
                user_profile.picture = request.FILES['picture']
            else:
                user_profile.picture = 'img/user_avatar.png'
            user_profile.save()

            # Fan/Band Profile
            if user_type == 'fan':
                profile = FanProfile.objects.get_or_create(profile=user_profile)
            else:
                profile = BandProfile.objects.get_or_create(profile=user_profile)

            # Auto login.
            user_login(request)

            return HttpResponseRedirect('/')
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        context_dict['profile_form'] = profile_form
        context_dict['user_form'] = user_form
    
    return render(request, 'webapp/register.html', context_dict)


def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        user_profile = UserProfile.objects.get(user=user)

        if 'picture' in request.FILES:
            user_profile.picture = request.FILES['picture']
        if request.POST['name'] != '':
            user_profile.name = request.POST['name']
        if request.POST['website'] != '':
            user_profile.website = request.POST['website']
        if 'city' in request.POST:
            user_profile.city = request.POST['city']
        if 'genre' in request.POST:
            user_profile.genre = request.POST['genre']
        user_profile.save()

        return HttpResponseRedirect('/')

    return render(request, 'webapp/edit_profile.html', {})


@login_required
def password_change(request):
    dict = {}
    if request.method == 'POST':
        try:
            current_password = request.POST['current_password']
            new_password = request.POST['new_password']
            repeat_password = request.POST['repeat_password']
        except:
            dict['error_message'] = 'All the fields must be provided.'
        
        if authenticate(username=request.user.username, password=current_password) and new_password == repeat_password:
            request.user.set_password(new_password)
            request.user.save()

            # Auto login with new details.
            user = authenticate(username=request.user.username, password=new_password)
            login(request, user)

            dict['success'] = 'Your password has been changed successfully.'
        else:
            dict['error_message'] = 'Some of the details you provided were wrong.'

        user_login(request)
    return render(request, 'webapp/password_change.html', dict)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def events(request):
    return render(request, 'webapp/events.html', {'events': Event.objects.all()})


def event(request, event_name):
    context_dict = {}
    try:
        l = visits[event]
    except:
        l = []
    try:
        event = Event.objects.get(slug=event_name)
    except:
        event = None

    if request.method == 'POST':
        profile = UserProfile.objects.get(user=request.user)
        try:
            fan = FanProfile.objects.get(profile=profile)
        except:
            pass
        if 'achievement' in request.POST:
            try:
                name = '+25xp for going to a gig %s' % event.name
                achievement = Achievement.objects.create(fan=fan, name=name)
                fan.xp += 25
                fan.save()
                visits[event] = l + [request.user]
            except:
                pass
        else:
            comment_form = None
            try:
                comment_form = CommentForm(data=request.POST)
            except:
                pass

            if comment_form:
                comment = comment_form.save(commit=False)
                comment.event = event
                comment.user = profile
                comment.save()
                try:      
                    name = '+10xp for writing a comment about a gig %s' % event.name
                    achievement = Achievement.objects.create(fan=fan, name=name)
                    fan.xp += 10
                    fan.save()
                except:
                    pass
    if event:
        event.views += 1
        event.save()
        try:
            comments = Comment.objects.filter(event=event).order_by('date')
            context_dict['comments'] = comments
        except:
            pass
        context_dict['event'] = event
    else:
        return HttpResponseRedirect('/create_event/')
    try:
        context_dict['visited'] = visits[event]
    except:
        pass
    return render(request, 'webapp/event.html', context_dict)


@login_required
def fan(request, username):
    context_dict = {}
    try:
        user = User.objects.get(username=username)
        profile = UserProfile.objects.get(user=user)
        fan = FanProfile.objects.get(profile=profile)
        print 'fsn'
    except:
        fan = None

    if fan:
        context_dict['username'] = user
        context_dict['fan'] = fan
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
        profile = UserProfile.objects.get(user=user)
        band = BandProfile.objects.get(profile=profile)
    except:
        band = None

    if request.method == 'POST':
        feedback_form = None
        try:
            feedback_form = FeedbackForm(data=request.POST)
        except:
            pass
        fan_profile = UserProfile.objects.get(user=request.user)
        fan = FanProfile.objects.get(profile=fan_profile)
        if feedback_form:
            feedback = feedback_form.save(commit=False)
            feedback.band = band
            feedback.user = fan_profile
            feedback.save()
            name = '+50xp for leaving band %s a feedback.' % profile.name
            achievement = Achievement.objects.create(fan=fan, name=name)
            fan.xp += 50
            fan.save()

    if band:
        context_dict['username'] = request.user
        context_dict['band'] = band
        context_dict['profile'] = profile
        if user == request.user:
            context_dict['logged_in'] = True
    else:
        return HttpResponseRedirect('/register/band/')

    return render(request, 'webapp/band.html', context_dict)

def band_list(request):
    context_dict = {}
    user_list = UserProfile.objects.all()
    band_list=[]
    for user in user_list:
        try:
            band=BandProfile.objects.get(profile=user)
            band_list += [user]
        except:
            pass
    context_dict['band_list'] = band_list
    return render(request, 'webapp/band_list.html', context_dict)

@login_required
def create_event(request):
    context_dict = {}
    try:
        profile = UserProfile.objects.get(user=request.user)
        band = BandProfile.objects.get(profile=profile)
    except:
        band = None

    if request.method == 'POST':
        if band:
            event_form = EventForm(data=request.POST)
            if event_form.is_valid():
                event = event_form.save(commit=False)
                event.band = band
                if 'picture' in request.FILES:
                    event.picture = request.FILES['picture']
                else:
                    event.picture = 'img/gig_logo.jpg'

                event.save()

                return HttpResponseRedirect('/event/%s' % event.slug)
            else:
            
				print event_form.errors
    else:
        if band:
            event_form = EventForm()
            context_dict['event_form'] = event_form
        else:
            context_dict['error'] = 'Only bands can create new events.'

    return render(request, 'webapp/create_event.html', context_dict)

def achievements(request):
    context_dict = {}
    try:
        profile = UserProfile.objects.get(user=request.user)
        fan = FanProfile.objects.get(profile=profile)
        achievements = Achievement.objects.filter(fan=fan)
        context_dict['achievements'] = achievements
    except:
        pass
    return render(request, 'webapp/achievements.html', context_dict)


# Sends context info to all the templates
def get_context_info(request):

    context = {}
    context['cities'] = CITIES
    context['genres'] = GENRES

    # Current user info
    try:
        user = request.user
        user_profile = UserProfile.objects.get(user=user)
    except:
        pass
    try:
        profile = FanProfile.objects.get(profile=user_profile)
        context['xps'] = profile.xp/30
        context['user_type'] = 'fan'
    except:
        pass
    try:
        profile = BandProfile.objects.get(profile=user_profile)
        context['user_type'] ='band'
    except:
        pass


    # Lists of bands and fans
    bands = BandProfile.objects.all()
    context['bands'] = bands
    fans = FanProfile.objects.all()
    context['fans'] = fans

    # List of all user profiles
    user_profiles = UserProfile.objects.all()
    context['user_profiles'] = user_profiles

    # Lists of fan and band user profiles
    fan_profiles = []
    band_profiles = []
    for profile in user_profiles:
        try:
            fan_profile = FanProfile.objects.get(profile=profile)
            fan_profiles += [profile]
        except:
            pass
        try:
            band_profile = BandProfile.objects.get(profile=profile)
            band_profiles += [profile]
        except:
            pass
    context['fan_profiles'] = fan_profiles
    context['band_profiles'] = band_profiles

    return context
