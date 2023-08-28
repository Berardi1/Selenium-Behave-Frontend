from behave import *


@when(u'I open a product')
def step_impl(context):
    context.product_store_page.open_product()


@then(u'I should see the product details')
def step_impl(context):
    message = context.product_store_page.get_description()
    expected_message = f"Product description"
    assert message == expected_message, f"Expected message: '{expected_message}', Actual message: '{message}'"


@when(u'I added the product to the cart')
def step_impl(context):
    context.product_store_page.add_product_to_cart()
