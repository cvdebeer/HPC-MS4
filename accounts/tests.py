# from django.test import TestCase
# from .models import User, Profile


# class TestProfile(TestCase):

#     def test_profile_defaults(self):
#         def setUp(self):
#             user = User.objects.create(name='TestUser', email='test@test.com',
#                                        password1='Test123', password2='Test123', first_name='John', last_name='Doe')
#             Profile.objects.create(user=user)

#         def test_profile_defaults(self):
#             user = User.objects.get(name='TestUser')
#             item = Profile.objects.get(user=user)
#             user.save()
#             item.save()

#             self.assertTrue(item.image)
#             self.assertFalse(item.testimonial)
#             self.assertEqual(item.name, 'TestUser')
#             self.assertEqual(item.email, 'test@test.com')
#             self.assertEqual(item.password1, 'Test123')
#             self.assertEqual(item.password2, 'Test123')
#             self.assertEqual(item.first_name, 'John')
#             self.assertEqual(item.last_name, 'Doe')
