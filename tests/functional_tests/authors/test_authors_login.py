from .base import AuthorsBaseTest
import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from selenium.webdriver.common.by import By

@pytest.mark.functional_test
class AuthorsLoginTest(AuthorsBaseTest):
    def test_user_valid_data_can_login_successfully(self):
        string_password = 'pass'
        user = User.objects.create_user(username='My_user', password=string_password)

        # User open the login page
        self.browser.get(self.live_server_url + reverse('authors:login'))

        # User see login form
        form = self.browser.find_element(By.CLASS_NAME, 'main-form')
        username_field = self.get_by_placeholder(form, 'Type your username')
        password_field = self.get_by_placeholder(form, 'Type your password')

        # username enter your username and password 
        username_field.send_keys(user.username)
        password_field.send_keys(string_password)

        # User send the form
        form.submit()

        # User see login success mesage with your user
        self.assertIn(
            f'You are logged in with {user.username}.',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )

        # End Test

    def test_login_create_raises_404_if_not_POST_method(self):
        self.browser.get(self.live_server_url + reverse('authors:login_create'))

        self.assertIn(
            'Not Found',
            self.browser.find_element(By.TAG_NAME, 'body').text
            )
        
    def test_form_login_is_valid(self):
        # User open the login page  
        self.browser.get(
            self.live_server_url + reverse('authors:login')
        )

        # USer see login form
        form = self.browser.find_element(By.CLASS_NAME, 'main-form')

        # and try send values empyts
        username = self.get_by_placeholder(form, 'Type your username')
        password = self.get_by_placeholder(form, 'Type your password')
        username.send_keys(' ')
        password.send_keys(' ')

        # User send the form
        form.submit()

        # See the error message
        self.assertIn(
            'Invalid username or password',
            self.browser.find_element(By.TAG_NAME, 'body').text
             
        )

    def test_form_login_invalid_credentials(self):
        # User open the login page  
        self.browser.get(
            self.live_server_url + reverse('authors:login')
        )

        # USer see login form
        form = self.browser.find_element(By.CLASS_NAME, 'main-form')

        # and try send values with data that not corresponding
        username = self.get_by_placeholder(form, 'Type your username')
        password = self.get_by_placeholder(form, 'Type your password')
        username.send_keys('invalid_user')
        password.send_keys('invalid_password')

        # User send the form
        form.submit()

        # See the error message
        self.assertIn(
            'Invalid Credentials',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )

    