import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'discoveragig.settings')

import django
django.setup()

from webapp.models import BandProfile, FanProfile, Achievement, Event, Comment, Feedback, Rating
from django.contrib.auth.models import User


def populate():
	PASSWORD = '1234'

	# Test Bands
	band_act = add_band('act', PASSWORD, 'Act', 'Hey everyone!', 30, 'ED', 'metal')
	band_one = add_band('one', PASSWORD, 'One', 'This is the best band.', 13, 'GL', 'rock')
	band_random = add_band('random', PASSWORD, 'RDom')

	# Test Fans
	fan_roger = add_fan('roger', PASSWORD, 99, 1, 'GL', 'pop')
	fan_bob = add_fan('bobybob', PASSWORD, 1001, 0, 'ED', 'rock')
	fan_spinner = add_fan('spinner', PASSWORD)

	# Test Events
	event_act = add_event(band_act, 'First Act Concert', 17.0, 'GL', 'GUU Venue', 35, 5)
	event_act2 = add_event(band_act, 'Second Act Concert', 10.0, 'ED', 'Edinburgh Uni', 150, 200)
	event_random = add_event(band_random, 'RandomRandom!!!', 5, 'AB', 'Aberdeen venue', 3, 25)
	event_one = add_event(band_one, 'One', 7, 'GL', 'Park', 81, 0)

	#Test Achievements
	ac_1 = add_achievement(fan_spinner)
	ac_2 = add_achievement(fan_spinner, 'LC', 25)
	ac_3 = add_achievement(fan_bob)
	ac_4 = add_achievement(fan_roger)
	ac_5 = add_achievement(fan_roger, 'WG', 10)

	#Test Comments
	tc_1 = add_comment(fan_roger.user, event_one, 'Best performance by my favourite band ONE.')
	tc_2 = add_comment(fan_spinner.user, event_random, 'Expected something slightly better...')
	tc_3 = add_comment(fan_bob.user, event_act, 'Amazing!!! Hope the second concert will be just as great.')
	tc_4 = add_comment(fan_spinner.user, event_one, 'Good.')
	tc_5 = add_comment(fan_bob.user, event_act2, 'Superb! Just like the first concert.')
	tc_6 = add_comment(fan_roger.user, event_act, 'Yeeeeeeeessssss.')

	#Test Feedbacks
	tf_1 = add_feedback(fan_bob.user, band_one, 'My favourite band!!!')
	tf_2 = add_feedback(fan_roger.user, band_act, 'Good stuff.')
	tf_3 = add_feedback(fan_roger.user, band_random, 'Whatever...')
	tf_4 = add_feedback(fan_spinner.user, band_act, 'Yes, YEs, YEsssssss')
	tf_5 = add_feedback(fan_roger.user, band_random, 'SO RANDOM!')

	print 'Database has been successfully populated.'

def add_band(username, password, band_name, mood='', views=0, city='GL', genre='rock'):
	user = User.objects.create_user(
		username = username,
		password = password,
		email = 'test@testband.com')

	band = BandProfile.objects.get_or_create(user=user, name=band_name)[0]
	band.mood = mood
	band.views = views
	band.city = city
	band.genre = genre
	band.save()
	return band


def add_fan(username, password, xp=0, title=0, city='GL', genre='rock'):
	user = User.objects.create_user(
		username = username,
		password = password,
		email = 'test@testfan.com')

	fan = FanProfile.objects.get_or_create(user=user)[0]
	fan.xp = xp
	fan.title = title
	fan.city = city
	fan.genre = genre
	fan.save()
	return fan


def add_event(band, event_name, price=0.0, city='GL', venue='', views=0, likes=0):
	event = Event.objects.get_or_create(band=band, name=event_name)[0]
	event.price = price
	event.city = city
	event.venue = venue
	event.views = views
	event.likes = likes
	event.save()
	return event


def add_achievement(fan, name='RG', xp=0):
	achievement = Achievement.objects.get_or_create(fan=fan)[0]
	achievement.name = name
	achievement.xp = xp
	achievement.save()
	return achievement


def add_comment(user, event, text):
	comment = Comment.objects.get_or_create(user=user, event=event, text=text)[0]
	return comment


def add_feedback(user, band, text):
	feedback = Feedback.objects.get_or_create(user=user, band=band, text=text)[0]
	return feedback

# Start execution here!
if __name__ == '__main__':
    print "Database is beeing populated..."
    populate()