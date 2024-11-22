import os
from dotenv import load_dotenv

load_dotenv()

def debug_bool_check():
    if os.getenv('DEBUG').lower() == 'true':
        return True
    return False

def get_allowed_hosts():
    allowed_hosts = os.getenv('ALLOWED_HOSTS')
    if not allowed_hosts or allowed_hosts == '':
        return ['localhost', '127.0.0.1']
    return allowed_hosts.split(', ')