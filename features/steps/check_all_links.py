from behave import *
use_step_matcher("re")


@given("I open PracticeSelenium website")
def step_impl(context):
    context.browser.get("http://www.practiceselenium.com")
    pass


@then("I print the title")
def step_impl(context):
    title = context.browser.title
    print(title, "\n")
    assert "Welcome" in title
    pass


@step("print the name")
def step_impl(context):
    print(context.browser.name)
    pass


@then("I print current url")
def step_impl(context):
    print(context.browser.current_url)
    pass


@step("I click Our Passion link")
def step_impl(context):
    context.browser.find_element_by_link_text("Our Passion").click()
    print(context.browser.title)
    assert "Our Passion" in context.browser.title
    pass


@then("I click back on the browser")
def step_impl(context):
    context.browser.back()
    pass


@step("I click forward on the browser")
def step_impl(context):
    context.browser.forward()
    pass


@step("I click refresh on the browser")
def step_impl(context):
    context.browser.refresh()
    pass


@step("I click Menu link")
def step_impl(context):
    context.browser.find_element_by_link_text("Menu").click()
    print(context.browser.title)
    assert "Menu" in context.browser.title
    pass


@step("I click Let's Talk Tea link")
def step_impl(context):
    context.browser.find_element_by_link_text("Let's Talk Tea").click()
    print(context.browser.title)
    assert "Let's Talk Tea" in context.browser.title
    pass


@step("I click Check Out link")
def step_impl(context):
    context.browser.find_element_by_link_text("Check Out").click()
    print(context.browser.title)
    assert "Check Out" in context.browser.title
    pass