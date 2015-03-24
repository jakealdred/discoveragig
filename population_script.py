import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'discoveragig.settings')

import django
django.setup()

from webapp.models import UserProfile, BandProfile, FanProfile, Event, Comment, Feedback
from django.contrib.auth.models import User


def populate():
	PASSWORD = '0000'

	# Test Bands
	print 'Adding Bands'
	band_act = add_band('act', PASSWORD, 'The Act', 'Glasgow', 'BritPop', 'profile_images/band.jpeg')
	band_one = add_band('one', PASSWORD, 'Band One', 'Edinburgh', 'Rock', 'profile_images/bs.png')
	band_random = add_band('random', PASSWORD, 'RDom', 'Aberdeen', 'BritPop', 'profile_images/band.jpeg')
	band_best = add_band('best', PASSWORD, 'BestBest', 'Glasgow', 'Alternative', 'profile_images/bs.png')

	# Test Fans
	print 'Adding Fans'
	fan_roger = add_fan('roger', PASSWORD, 'Roger', 'Edinburgh', 'BritPop', 'profile_images/bs.png')
	fan_bob = add_fan('bobybob', PASSWORD, 'Robert', 'Glasgow', 'Alternative', 'profile_images/gb.png')
	fan_spinner = add_fan('spinner', PASSWORD, 'Steven', 'Glasgow', 'Metal', 'profile_images/lm.jpg')

	# Test Events
	print 'Adding Events'
	event_act = add_event(band_act, 'First Act Concert', 'Glasgow', 'BritPop', 'Glasgow Concert Hall', '2015-05-13',
						'Come to see the gig of this new and amazing band!!!', 71, 'cn1.jpg')
	event_act2 = add_event(band_act, 'Second Act Concert', 'Glasgow', 'Rock', 'Glasgow Hall', '2015-04-13',
						'Come to see us this weekend!', 0, 'cn2.jpeg')
	event_random = add_event(band_random, 'RandomRandom!!!', 'Aberdeen', 'Alternative', 'The Hall', '2015-05-02',
						'Great concert by a great band!!!', 21, 'cn1.jpg')
	event_best = add_event(band_best, 'This week The Best', 'Glasgow', 'Rock', 'GUU', '2016-01-17',
						'This weekend in GUU, we are waiting to see YOU!', 3, 'cn1.jpg')
	event_one = add_event(band_one, 'One', 'Glasgow', 'Metal', 'QMU', '2015-12-01',
						'The Park', 77, 'cn2.jpeg')


	#Test Comments
	print 'Adding Comments'
	tc_1 = add_comment(fan_roger.profile, event_one, 'Best performance by my favourite band ONE.', '2015-03-01')
	tc_2 = add_comment(fan_spinner.profile, event_random, 'Expected something slightly better...', '2015-01-01')
	tc_3 = add_comment(fan_bob.profile, event_act, 'Amazing!!! Hope the second concert will be just as great.', '2015-03-13')
	tc_4 = add_comment(fan_spinner.profile, event_one, 'Good.', '2015-02-14')
	tc_5 = add_comment(fan_bob.profile, event_act2, 'Superb! Just like the first concert.', '2015-03-24')
	tc_6 = add_comment(fan_roger.profile, event_act, 'Yeeeeeeeessssss.', '2015-01-01')
	tc_7 = add_comment(fan_spinner.profile, event_best, 'Really good gig.', '2015-02-03')
	tc_8 = add_comment(fan_roger.profile, event_act2, 'Such an amazing event.', '2015-02-06')
	tc_9 = add_comment(fan_bob.profile, event_best, 'The last one was great. So was this on. Good job guys! Keep it up.', '2015-02-13')

	#Test Feedbacks
	print 'Adding Feedbacks'
	tf_1 = add_feedback(fan_bob.profile, band_one, 'My favourite band!!!', '2015-01-17')
	tf_2 = add_feedback(fan_roger.profile, band_act, 'Good stuff.', '2015-01-13')
	tf_3 = add_feedback(fan_roger.profile, band_random, 'Whatever...', '2015-02-01')
	tf_4 = add_feedback(fan_spinner.profile, band_act, 'Yes, YEs, YEsssssss', '2015-03-03')
	tf_5 = add_feedback(fan_roger.profile, band_random, 'SO RANDOM!', '2015-03-24')



def add_band(username, password, name, city, genre, picture):
	user = User.objects.create_user(
		username = username,
		password = password,
		email = 'test@testband.com')

	profile = UserProfile.objects.get_or_create(user=user)[0]
	profile.name = name
	profile.city = city
	profile.genre = genre
	profile.website = 'http://www.band.com'
	profile.picture = picture
	profile.save()
	band = BandProfile.objects.create(profile=profile)
	return band


def add_fan(username, password, name, city, genre, picture):
	user = User.objects.create_user(
		username = username,
		password = password,
		email = 'test@testfan.com')

	profile = UserProfile.objects.get_or_create(user=user)[0]
	profile.name = name
	profile.city = city
	profile.genre = genre
	profile.website = 'http://www.fan.com'
	profile.picture = picture
	profile.save()
	fan = FanProfile.objects.create(profile=profile)
	return fan


def add_event(band, name, city, genre, venue, date, description, views, picture):
	event = Event.objects.get_or_create(band=band, name=name)[0]
	event.city = city
	event.genre = genre
	event.venue = venue
	event.views = views
	event.date = date
	event.description = description
	event.website = 'event@suchevent.com'
	event.picture = picture
	event.save()
	return event


def add_comment(user, event, text, date):
	comment = Comment.objects.get_or_create(user=user, event=event, text=text)[0]
	comment.date = date
	comment.save()
	return comment


def add_feedback(user, band, text, date):
	feedback = Feedback.objects.get_or_create(user=user, band=band, text=text)[0]
	feedback.date = date
	feedback.save()
	return feedback

# Start execution here!
if __name__ == '__main__':
    print "Database is beeing populated..."
    populate()
    print "Finished."