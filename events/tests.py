from django.test import TestCase
from .models import Event, EventType


class TestEventTypeModel(TestCase):
    def test_defaults(self):
        item = EventType(name='event')
        item.save()
        self.assertEqual(item.name, 'event')
        self.assertFalse(item.category)
        self.assertFalse(item.description)
        self.assertEqual(item.cost_participant, 0)
        self.assertEqual(item.cost_non_participant, 0)
        self.assertEqual(item.cost_trainee, 0)

    def test_categories(self):
        item = EventType(name='event', category='Training')
        item.save()
        self.assertTrue(item.category)
        self.assertEqual(item.category, 'Training')

    def test_description(self):
        item = EventType(name='event', description='Testing')
        item.save()
        self.assertTrue(item.description)
        self.assertEqual(item.description, 'Testing')

    def test_costs(self):
        item = EventType(name='event', cost_participant=10.00,
                         cost_non_participant=20.00, cost_trainee=1)
        item.save()
        self.assertEqual(item.cost_participant, 10.00)
        self.assertEqual(item.cost_non_participant, 20.00)
        self.assertEqual(item.cost_trainee, 1.00)


class TestEventModel(TestCase):
    def setUp(self):
        event = EventType.objects.create(name='event', category='Training')
        Event.objects.create(event=event)

    def test_event_defaults(self):
        event = EventType.objects.get(name='event', category='Training')
        item = Event.objects.get(event=event)
        event.save()
        item.save()
        self.assertTrue(item.event)
        self.assertTrue(item.date_start)
        self.assertTrue(item.date_end)
        self.assertTrue(item.time_start)
        self.assertTrue(item.time_end)
        self.assertEqual(
            item.location, 'The Ridge Wellness Center, 1 Ateljee Street, Randpark Ridge')
        self.assertEqual(item.facilitator, 'Sonja Simak')
        self.assertEqual(item.max_attendees, 15)

    def test_dates(self):
        event = EventType.objects.get(name='event', category='Training')
        item = Event(event=event, date_start='2020-01-01',
                     date_end='2020-01-01')
        self.assertEqual(item.date_start, '2020-01-01')
        self.assertEqual(item.date_end, '2020-01-01')

    def test_times(self):
        event = EventType.objects.get(name='event', category='Training')
        item = Event(event=event, time_start='14:00',
                     time_end='16:00')
        self.assertEqual(item.time_start, '14:00')
        self.assertEqual(item.time_end, '16:00')

    def test_location(self):
        event = EventType.objects.get(name='event', category='Training')
        item = Event(event=event, location='Test location')
        self.assertEqual(item.location, 'Test location')

    def test_facilitator(self):
        event = EventType.objects.get(name='event', category='Training')
        item = Event(event=event, facilitator='Test facilitator')
        self.assertEqual(item.facilitator, 'Test facilitator')

    def test_maximum_attendees(self):
        event = EventType.objects.get(name='event', category='Training')
        item = Event(event=event, max_attendees=7)
        self.assertEqual(item.max_attendees, 7)
