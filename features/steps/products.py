from behave import *

@given(u'Im logged in')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Im logged in')


@when(u'I open a product')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I open a product')


@then(u'I should see the product details')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see the product details')


@when(u'I added the product to the cart')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I added the product to the cart')


@then(u'I should see the "Product added." alert message')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see the "Product added." alert message')
