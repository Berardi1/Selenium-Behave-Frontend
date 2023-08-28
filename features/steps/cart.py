from behave import *


@given(u'I add a product to the cart')
def step_impl(context):
    context.execute_steps(''' When I open a product
        And I added the product to the cart
        Then I should get a "Product added" alert
    ''')


@then(u'I should see the product')
def step_impl(context):
    message = context.cart_page.is_product_at_position()
    expected_message = f"Delete"
    assert message == expected_message, f"Expected message: '{expected_message}', Actual message: '{message}'"


@when(u'I open the cart')
def step_impl(context):
    context.cart_page.open_cart()


@when(u'I place the order')
def step_impl(context):
    context.cart_page.place_order()


@when(u'purchase the order')
def step_impl(context):
    personal_information = {
        'name': 'Berardi',
        'country': 'Argentina',
        'city': 'Ucacha',
        'credit_card': '123456789',
        'month': '12',
        'year': '2023'
    }
    context.cart_page.purchase_order(personal_information)


@then(u'I should see that the purchase is confirmed')
def step_impl(context):
    message = context.cart_page.purchase_confirm()
    expected_message = f'Thank you for your purchase!'
    assert message == expected_message, f"Expected message: '{expected_message}', Actual message: '{message}'"


@when(u'I remove the first product')
def step_impl(context):
    context.cart_page.remove_product()


@then(u'I should see that a product was removed')
def step_impl(context):
    message = context.cart_page.is_element_not_present
    expected_message = f"Delete"
    assert message != expected_message, f"Expected message: '{expected_message}', Actual message: '{message}'"


