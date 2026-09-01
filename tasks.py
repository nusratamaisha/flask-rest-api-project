import os
import requests
import jinja2

from dotenv import load_dotenv

load_dotenv()
DOMAIN = os.getenv("MAILGUN_DOMAIN")

template_loader = jinja2.FileSystemLoader("templates")
template_env = jinja2.Environment(loader=template_loader)


def render_template(template_filename, **context):
    return template_env.get_template(template_filename).render(**context)


def send_simple_message(to, subject, body, html):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox7a72e6a9375741a9bf51e4b8cc9e16ef.mailgun.org/messages",
        auth=("api", os.getenv("MAILGUN_API_KEY")),
        data={
            "from": "Mailgun Sandbox <postmaster@sandbox7a72e6a9375741a9bf51e4b8cc9e16ef.mailgun.org>",
            "to": to,
            "subject": subject,
            "text": body,
            "html":html,
        },
    )


def send_user_registration_email(email, username):
    return send_simple_message(
        email,
        "Successfully signed up",
        f"Hi {username}! You have successfully signed up to the Stores REST API.",
        render_template("email/action.html", username=username),
    )