from datetime import datetime
from allure_commons.types import AttachmentType
from allure_commons._allure import Attach
from behave.log_capture import capture
from features.pages.home_page import *
import allure

def before_all(context):
    context.browser = Browser()
    context.home_page = HomePage()
    # context.config.setup_logging(configfile="test.ini", filename="AppLog.log")
    print("Executing before all\n")


"""
def before_feature(context, feature):
    context.browser = Browser()
    context.home_page = HomePage()
    context.browser.delete_cookies()
    print("Before feature\n")


# Scenario level objects are popped off context when scenario exits
def before_scenario(context, scenario):
    print("Before scenario\n")


def after_feature(context, feature):
    print("\nAfter feature")

"""
@capture
def before_scenario(context, scenario):
    if "skip" in scenario.effective_tags:
        scenario.skip("Marked with @skip")
        return
    else:
        print("\n----------------------------------------------\n")
        print("Scenario: {}\n".format(scenario.name))
        print("----------------------------------------------\n")



def before_step(context, step):
    print("\nStep: {}".format(step.name))



def after_step(context, step):
    #print("\n")
    print("\nStatus step: {}\n".format(step.status))

    hours = datetime.now().strftime("%H")
    hours = int(hours) - 3
    time = datetime.now().strftime("%m-%d-%Y_{}:%M:%S").format(hours)
    # print(time_failed)
    if step.status == "failed":

        Attach.__call__(context, body=context.home_page.get_screenshot_png(), name="Failed step - {}".format(time),
                      attachment_type=AttachmentType.PNG)
    else:
        Attach.__call__(context, body=context.home_page.get_screenshot_png(),
                        name="Failed pass - {}".format(time),
                        attachment_type=AttachmentType.PNG)

def after_scenario(context, scenario):
    print("\n----------------------------------------------\n")
    print("Delete cookies")
    sleep(10)
    #context.browser.delete_cookies()
    print("\n----------------------------------------------\n")
    #context.home_page.clear_cache_chrome()


def after_all(context):
    context.browser.delete_cookies()
    context.browser.close()
    # print("Executing after all")


