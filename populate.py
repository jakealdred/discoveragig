import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'discoveragig.settings')

import django
django.setup()

from webapp.models import BandProfile, FanProfile, Achievement, Event, Comment
from django.contrib.auth.models import User


def populate():
    band_act = add_band('useract', 'Act')

def add_band(username, password, name):
    #user = User.objects.get_or_create(username=username, first_name=name)
    band = BandProfile.objects.get_or_create(user=user)[0]
    

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()