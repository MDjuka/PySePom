import string
import random
import logging as logger


def generate_random_email_and_password(domain=None, email_prefix=None):
    if not domain:
        domain = "yahoo.com"
    if not email_prefix:
        email_prefix = "testuser"

    # to generate random email
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(8)).lower()
    email = random_string + "@" + domain
    logger.info("Generated random email")

    # to generate random password
    rand_pwd = ''.join(random.choice(string.ascii_letters) for i in range(15))
    random_info = {"email": email, "password": rand_pwd}
    return random_info