from behave import *
from google.cloud import storage as gcs

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@when('we implement a test2')
def step_impl(context):
    print("hello, multiple scenario")
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    x()

def x():
    b = gcs.Client().bucket("dmt-auto-seo")
    print(f"b: {b}")
    o = b.blob("config/gcb_test")
    print(f"o: {o}")
    print(f"o.exists: {o.exists()}")
    assert o.exists()
