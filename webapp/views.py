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

    # Gather the username and password provided by the user.
    # This information is obtained from the login form.
            # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
            # because the request.POST.get('<variable>') returns None, if the value does not exist,
            # while the request.POST['<variable>'] will raise key error exception
    username = request.POST.get('username')
    password = request.POST.get('password')

    # Use Django's machinery to attempt to see if the username/password
    # combination is valid - a User object is returned if it is.
    user = authenticate(username=username, password=password)

    # If we have a User object, the details are correct.
    # If None (Python's way of representing the absence of a value), no user
    # with matching credentials was found.
    if user:
        # Is the account active? It could have been disabled.
        if user.is_active:
            # If the account is valid and active, we can log the user in.
            # We'll send the user back to the homepage.
            login(request, user)
            return 'Success'
        else:
            # An inactive account was used - no logging in!
            return "Your Rango account is disabled."
    else:
        # Bad login details were provided. So we can't log the user in.
        print "Invalid login details: {0}, {1}".format(username, password)
        return "Invalid login details supplied."


def register(request, user_type):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False
    context_dict = {}
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        band_form = None
        fan_form = None
        user_form = UserForm(data=request.POST)
        if user_type == 'band':
            form = BandProfileForm()
        elif user_type == 'fan':
            form = FanProfileForm()
        
        # If the two forms are valid...
        if user_form.is_valid() and form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = form.save(commit=False)
            profile.user = user

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, form.errors

        return HttpResponseRedirect('/')
    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
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
    context_dict['registered'] = registered
    # Render the template depending on the context.
    return render(request,
            'webapp/register.html',
            context_dict)


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')



