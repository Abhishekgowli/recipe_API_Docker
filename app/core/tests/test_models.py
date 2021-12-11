from django.test import TestCase
from django.contrib.auth import get_user_model
class ModelTests(TestCase):


    def test_create_user_with_email_successful(self):
        """Test Creating a new User with an email is  successful"""
        email="gowleabhi@gmail.com"
        password="Testpass123"
        user=get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
    
    def test_new_user_email_normalize(self):
        """test the email for new user to normilized"""
        email="test@GMAIL.COM"
        user=get_user_model().objects.create_user(email,'test123')

        self.assertEqual(user.email,email.lower())
    
    def test_new_user_invalid_email(self):
        "Test the User without email"
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test1234')
    
    def test_createsuper_user_with_email_succcessfuly(self):
        "Test the Creating a superUser"
        email="test12@gmail.com"
        password="test1234"
        user=get_user_model().objects.create_supperuser(email=email, password=password)
        self.assertTrue(user.is_supperuser)
        self.assertTrue(user.is_staff)
