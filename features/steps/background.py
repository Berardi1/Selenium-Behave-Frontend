from behave import given


@given(u"I navigate to Demoblaze")
def step_impl(context):
    context.base_page.visit_web(context.config.userdata['base_url'])
