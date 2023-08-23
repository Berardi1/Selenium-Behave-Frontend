from behave import *


@given(u'I am logged in')
def step_impl(context):
    context.execute_steps('''
        When I open the login modal
        And I enter valid email and password into the fields
        Then I should be correctly logged in
    ''')


@when(u'I open the login modal')
def step_impl(context):
    context.login_page.open_login_modal


@when(u'I enter valid email and password into the fields')
def step_impl(context):
    # to improve
    credentials = {
        'username': 'Berardi',
        'password': 'contraseña'
    }
    context.login_page.login_credentials(credentials)


@then(u'I should be correctly logged in')
def step_impl(context):
    message = context.login_page.get_welcome_text()
    expected_message = f'Welcome Berardi'
    assert message == expected_message, f"Expected message: '{expected_message}', Actual message: '{message}'"


@when(u'I enter invalid email and valid password into the fields')
def step_impl(context):
    # to improve
    credentials = {
        'username': 'Random',
        'password': 'contraseña'
    }
    context.login_page.login_credentials(credentials)


@when(u'I enter valid email and invalid password into the fields')
def step_impl(context):
    # to improve
    credentials = {
        'username': 'Berardi',
        'password': 'random'
    }
    context.login_page.login_credentials(credentials)


@when(u'I enter invalid email and invalid password into the fields')
def step_impl(context):
    # to improve
    credentials = {
        'username': 'random',
        'password': 'random'
    }
    context.login_page.login_credentials(credentials)


@when(u'I dont enter anything into email and password fields')
def step_impl(context):
    # to improve
    credentials = {
        'username': '',
        'password': ''
    }
    context.login_page.login_credentials(credentials)


@then(u'I should get a "{message}" alert')
def step_impl(context, message):
    alert_text = context.base_page.get_alert_text()
    expected_message = message
    assert alert_text == expected_message, f"Expected alert: '{expected_message}', Actual alert: '{alert_text}'"
