Behave
==================

You need Firefox installed https://www.mozilla.org/en-GB/firefox/new/

Do you need to upgrade Geckodriver?

    brew upgrade geckodriver

## Installation

Python3 https://www.python.org/downloads/

pip https://pypi.org/project/pip/

    pip install pip

Selenium is used to automate web browser interaction from Python https://pypi.org/project/selenium/

    pip install selenium

Splinter is an abstraction layer on top of existing browser automation tools such as Selenium https://splinter.readthedocs.io/en/latest/install.html

    pip install splinter

Behave https://behave.readthedocs.io/

    pip install behave
    
Behaving is a web application testing framework for Behavior-Driven-Development, based on behave and splinter https://pypi.org/project/behaving

    pip install behaving

## Environment variables

The test suite uses the following environment variables.
* `USER_EMAIL`: email address
* `USER_PASSWORD`: password

Create an env.py file and place it in the 'features' directory.

Format of env.py file:
```
os.environ['USER_EMAIL'] = 'email_address@gmail.com'
os.environ['USER_PASSWORD'] = 'password'
```

## Running the Behave tests

From the directory where you cloned the repo, this command will run the feature with all the Behave tests:

    behave

To run a specific scenario within the feature, use the line number, for example:

    behave features/sample.feature:27 

To debug the tests, you can add the following step:

    When I pause the tests
