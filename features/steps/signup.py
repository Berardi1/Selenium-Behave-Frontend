from behave import *


@when(u'I open the signup field')
def step_impl(context, modal):
    context.signup_page.open_signup_modal(modal)


@when(u'I enter all my fields')
def step_impl(context):
    # to improve
    credentials = {
        'username': 'Berardi',
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
