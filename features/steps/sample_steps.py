from behave import when
from behaving.web.steps import *
from behaving.sms.steps import *
from behaving.mail.steps import *
from behaving.notifications.gcm.steps import *
from behaving.personas.steps import *

@then('I should see the google page has loaded')
def step_impl(context):
    assert context.browser.find_by_text('Google')

@given('I use my email address to attempt to sign into google')
def step_impl(context):
    context.execute_steps('''
        Given a browser
        When I visit "https://google.com"
        And I press "Sign in"
    ''')
    context.browser.find_by_css('#identifierId').fill(f"{os.environ['USER_EMAIL']}")
    context.browser.find_by_css('.VfPpkd-LgbsSe').click()

@then('I should see that I should try a different browser to sign in')
def step_impl(context):
    assert context.browser.find_by_text('Try using a different browser. If you’re already using a supported browser, you can refresh your screen and try again to sign in.')
    