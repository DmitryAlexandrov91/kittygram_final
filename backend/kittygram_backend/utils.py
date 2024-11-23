import os
from dotenv import load_dotenv

load_dotenv()


def debug_bool_check():
    if os.getenv('DEBUG'):
        if os.getenv('DEBUG').lower() == 'true':
            return True
    return False


def get_allowed_hosts():
    allowed_hosts = os.getenv('ALLOWED_HOSTS', 'localhost, 127.0.0.1')
    return [host.strip() for host in allowed_hosts.split(',')]
