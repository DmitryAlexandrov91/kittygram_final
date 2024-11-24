import os
from dotenv import load_dotenv

load_dotenv()


def debug_bool_check():
    return os.getenv('DEBUG').lower() == 'true'


def get_allowed_hosts():
    allowed_hosts = os.getenv('ALLOWED_HOSTS', 'localhost, 127.0.0.1')
    return [host.strip() for host in allowed_hosts.split(',')]
