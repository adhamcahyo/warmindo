# modules/custom_helpers.py

def calculate_square(x):
    return x * x

def generate_random_string(length):
    import random
    import string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
