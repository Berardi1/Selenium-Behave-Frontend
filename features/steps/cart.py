from behave import *


@given(u'I add a product to the cart ')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I open the cart')


@then(u'I should see the product')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see the product')


@when(u'I open the cart {modal}')
def step_impl(context, modal):
    context.cart_page.open_cart(modal)


@when(u'purchase the order')
def step_impl(context):
    raise NotImplementedError(u'STEP: When purchase the order')


@then(u'I should see that the purchase is confirmed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see that the purchase is confirmed')


@when(u'I remove the first product')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I remove the first product')


@then(u'I should see that a product was removed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see that a product was removed')
