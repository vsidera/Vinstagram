from django.test import TestCase
from .models import Image, Profile, Comment
from datetime import datetime
from django.contrib.auth.models import User



class ProfileTest(TestCase):
    ''' test class for Profile model'''
    def setUp(self):
        ''' method called before each test case'''
        self.user = User.objects.create_user(username='siderra')

    def tearDown(self):
        ''' method to clear all setup instances after each test run '''
        self.user.delete()

    def test_profile_creation(self):
        ''' method to test profile instance is created only once for each user '''
        self.assertIsInstance(self.user.profile, Profile)
        self.user.save()
        self.assertIsInstance(self.user.profile, Profile)
        

class TestImage(TestCase):
    ''' test class for image model '''
    def setUp(self):
        ''' method called before each test case'''
        self.test_user = User(username='tunyi', password='tunyi@123')
        self.test_user.save()
        self.test_profile = self.test_user.profile
        self.test_profile.save()

    def test_instance(self):
        ''' test method to ensure image instance creation '''
        self.assertTrue(isinstance(self.test_image, Image))

    def test_save(self):
        ''' test method to save image instance to db '''
        self.test_image.save_image()
        self.assertEqual(len(Image.objects.all()), 1)

    def tearDown(self):
        ''' method to clear all setup instances after each test run '''
        self.test_user.delete()
        Image.objects.all().delete()
