from entities.host import Host
from repository.sqlite_helper import *

HOSTS_TABLE = 'users'

def get_all_hosts():
    result = execute(f"select * from {HOSTS_TABLE}")
    return (Host.from_dict(item) for item in result)