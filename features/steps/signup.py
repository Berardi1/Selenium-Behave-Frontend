import string
import random

from behave import *


@when('I open the signup modal')
def step_impl(context):
    context.signup_page.open_signup_modal


@when(u'I enter all my fields')
def step_impl(context):
    base_username = 'Berardi'
    random_digits = ''.join(random.choice(string.digits) for _ in range(5))
    username = f'{base_username}{random_digits}'

    credentials = {
        'username': username,
        'password': 'contraseña'
    }

    context.signup_page.signup_credentials(credentials)


@when(u'I enter only a password')
def step_impl(context):
    # to improve
    credentials = {
        'username': '',
        'password': 'contraseña'
    }
    context.signup_page.signup_credentials(credentials)


@when(u'I enter only a username')
def step_impl(context):
    # to improve
    credentials = {
        'username': 'Berardi',
        'password': ''
    }
    context.signup_page.signup_credentials(credentials)


@when(u'I dont enter anything into the fields')
def step_impl(context):
    # to improve
    credentials = {
        'username': '',
        'password': ''
    }
    context.signup_page.signup_credentials(credentials)
