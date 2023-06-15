from behave import *

@when(u'I open the login modal')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I open the login modal')


@when(u'I enter valid email and password into the fields')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter valid email and password into the fields')


@then(u'I should be correctly logged in')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should be correctly logged in')


@when(u'I enter invalid email and valid password into the fields')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter invalid email and valid password into the fields')


@then(u'I should get a "User does not exist." alert')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should get a "User does not exist." alert')


@when(u'I enter valid email and invalid password into the fields')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter valid email and invalid password into the fields')


@then(u'I should get "Wrong password." alert')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should get "Wrong password." alert')


@when(u'I enter invalid email and invalid password into the fields')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter invalid email and invalid password into the fields')


@when(u'I dont enter anything into email and password fields')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I dont enter anything into email and password fields')


@then(u'I should get a "Please fill out Username and Password." alert')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should get a "Please fill out Username and Password." alert')