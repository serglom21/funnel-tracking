from flask import Flask
from sentry_sdk import init as sentry_init, start_transaction, set_user
from random import choice
from sentry_sdk import set_measurement
from random import uniform
import time
import sentry_sdk
from random import randint

app = Flask(__name__)
locales = ["Brazil", "United States", "Canada", "Germany", "United Kingdom"]
users = ["abc@example.com", "djh@example.com", "267g@example.com", "djw@example.com", "djw6@example.com"]

# Initialize Sentry SDK
sentry_init(
    dsn="https://747a58fe9fa0f123cb95b909943a3ace@o88872.ingest.us.sentry.io/4506510403960832",
    traces_sample_rate=1.0
    )

def get_current_transaction():
    return sentry_sdk.Hub.current.scope

def random_user_email():
    index = randint(0, len(users)-1)
    return users[index]

def random_delay(min_seconds, max_seconds):
    """Generates a random delay between min_seconds and max_seconds"""
    delay = uniform(min_seconds, max_seconds)
    time.sleep(delay)

def random_locale():
    index = randint(0, len(locales)-1)
    return locales[index]

@app.route('/launch')
def app_launch():
    with start_transaction(op="task", name="App Launch"):
        get_current_transaction().set_tag("locale", random_locale())
        set_user({"email": random_user_email()})
        random_delay(0.2, 1.5)  # Random delay between 0.2 and 1.5 seconds
        return "App Launched"

@app.route('/verse')
def verse_of_the_day():
    with start_transaction(op="task", name="Verse of the Day"):
        get_current_transaction().set_tag("locale", random_locale())
        set_user({"email": random_user_email()})
        random_delay(0.2, 1.5)
        return "Verse Read"

@app.route('/scripture')
def guided_scripture():
    with start_transaction(op="task", name="Guided Scripture"):
        get_current_transaction().set_tag("locale", random_locale())
        set_user({"email": random_user_email()})
        random_delay(0.2, 1.5)
        return "Scripture Read"

@app.route('/prayer')
def guided_prayer():
    with start_transaction(op="task", name="Guided Prayer"):
        get_current_transaction().set_tag("locale", random_locale())
        set_user({"email": random_user_email()})
        random_delay(0.2, 1.5)
        return "Prayer Read"

@app.route('/plan')
def plan_start():
    with start_transaction(op="task", name="Plan Started"):
        get_current_transaction().set_tag("locale", random_locale())
        set_user({"email": random_user_email()})
        random_delay(0.2, 1.5)
        raise Exception("Oops, could not complete plan")
        return "Plan Started"

@app.route('/donation')
def donation_given():
    with start_transaction(op="task", name="Donation Given"):
        get_current_transaction().set_tag("locale", random_locale())
        set_user({"email": random_user_email()})
        random_delay(0.2, 1.5)
        raise Exception("Oops, could not complete donation")
        return "Donation Made"

if __name__ == "__main__":
    app.run(debug=True)