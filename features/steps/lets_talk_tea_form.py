from behave import *
from pdb import set_trace

use_step_matcher("re")


@given("I open Let's Talk Tea page")
def step_impl(context):
    context.browser.get("http://www.practiceselenium.com/let-s-talk-tea.html")
    pass


@then("I complete the form")
def step_impl(context):

    name = context.browser.find_element_by_name("name")
    email = context.browser.find_element_by_name("email")
    subject = context.browser.find_element_by_name("subject")
    subject = context.browser.find_element_by_name("message")


@then("I leave name blank")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("I enter 256 character on name")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("I add number or symbol on name")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("I leave email blank")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("I fill incorrect email format")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("I submit")
def step_impl(context):
    button = context.browser.find_element_by_xpath('//*[@id="form_78ea690540a24bd8b9dcfbf99e999fea"]/div[1]/div[5]/input')
    button.click()
    set_trace()
#    context.browser.find_element_by_xpath('//*[@id="form_78ea690540a24bd8b9dcfbf99e999fea"]/div[1]/div[1]/input and @class="form-value form-value-invalid"')