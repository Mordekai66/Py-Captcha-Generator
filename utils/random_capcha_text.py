import string
import random

def random_captcha_text(length=4):
    text = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return text