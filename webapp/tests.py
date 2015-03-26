from django.test import TestCase
from webapp.models import Event, BandProfile, FanProfile, UserProfile, Feedback
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


def add_band(username, password, name, city, genre):
	user = User.objects.create_user(
		username = username,
		password = password,
		email = 'test@testband.com')

	profile = UserProfile.objects.get_or_create(user=user)[0]
	profile.name = name
	profile.city = city
	profile.genre = genre
	profile.save()
	band = BandProfile.objects.create(profile=profile)
	return band


def add_fan(username, password, name, city, genre):
	user = User.objects.create_user(
		username = username,
		password = password,
		email = 'test@testfan.com')

	profile = UserProfile.objects.get_or_create(user=user)[0]
	profile.name = name
	profile.city = city
	profile.genre = genre
	profile.save()
	fan = FanProfile.objects.create(profile=profile)
	return fan


def add_event(band, name, city, genre, date, views):
	event = Event.objects.get_or_create(band=band, name=name)[0]
	event.city = city
	event.genre = genre
	event.views = views
	event.date = date
	event.save()
	return event


def add_feedback(user, band, text, date):
	feedback = Feedback.objects.get_or_create(user=user, band=band, text=text)[0]
	feedback.date = date
	feedback.save()
	return feedback


# Tests for Models
class ModelTester(TestCase):

    def test_band_profile(self):
    	band = add_band('test_band1', '0000', 'BandName', 'Glasgow', 'BritPop')
    	self.assertEqual(band.profile.user.username, 'test_band1')
    	self.assertEqual(band.profile.name, 'BandName')
    	self.assertEqual(band.profile.city, 'Glasgow')
    	self.assertEqual(band.profile.genre, 'BritPop')


    def test_fan_profile(self):
    	fan = add_fan('test_fan1', '0000', 'FanName', 'City', 'BritPop')
    	self.assertEqual(fan.profile.user.username, 'test_fan1')
    	self.assertEqual(fan.profile.name, 'FanName')
    	self.assertEqual(fan.profile.city, 'City')
    	self.assertEqual(fan.profile.genre, 'BritPop')


    def test_slug_event_name(self):
    	band = add_band('test_band2', '0000', 'BandName', 'Glasgow', 'BritPop')
        event = add_event(band, "Test Event", "Glasgow", "BritPop", "2015-02-23", 15)
        self.assertEqual(event.slug, 'test-event')


    def test_feedback(self):
    	band = add_band('test_band5', '0000', 'BandName', 'Glasgow', 'BritPop')
    	fan = add_fan('test_fan2', '0000', 'FanName', 'City', 'BritPop')
    	feedback = add_feedback(fan.profile, band, 'Great Test Band', '2015-03-25')
    	feedback_list = Feedback.objects.filter(band=band)
    	self.assertEqual(len(feedback_list), 1)
    	self.assertEqual(feedback_list[0].text, 'Great Test Band')

    def test_negatve_case (self):
    	band = add_band('test_band4', '0000', 'BandName', 'Glasgow', 'BritPop')
        event1 = add_event(band, "TestEvent3", "Glasgow", "BritPop", "2015-02-23", -3)
        self.assertEqual((event1.views>=0), True)

    

class ViewsTester(TestCase):


    def test_events_with_events(self):
    	band = add_band('test_band3', '0000', 'BandName', 'Glasgow', 'BritPop')
        event1 = add_event(band, "TestEvent1", "Glasgow", "BritPop", "2015-02-23", 15)
        event2 = add_event(band, "TestEvent2", "Edinburgh", "Metal", "2015-07-23", 1)
        
        response = self.client.get(reverse('events'))
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'TestEvent1')
        self.assertContains(response, 'TestEvent2')
        self.assertEqual (len(response.context['events']),2)
    

    def test_fan_page(self):
    	fan = add_fan('test_fan3', '0000', 'FanName', 'City', 'BritPop')

        response = self.client.get(reverse('webapp.views.fan', args=('test_fan3',)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'FanName')


    def test_band_page(self):
		band = add_band('test_band4', '0000', 'BandName', 'Glasgow', 'BritPop')

		response = self.client.get(reverse('webapp.views.band', args=('test_band4',)))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'BandName')


    def test_changes_0_to_Free(self):
		band = add_band('test_band5', '0000', 'BandName', 'Glasgow', 'BritPop')
		event = add_event(band, "TestEvent1", "Glasgow", "BritPop", "2015-02-23", 0)
		event.price = 0.0
		event.save()
		response = self.client.get(reverse('webapp.views.event', args=('testevent1',)))
		self.assertContains(response, 'Free')