from behave import *


@when(u'I open a product')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I open a product')


@then(u'I should see the product details')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see the product details')


@when(u'I added the product to the cart')
def step_impl(context):
    context.product_store_page.add_product_to_cart()

