import time
from tools import system_info_check

get_routes = {
    "/": str(int(time.time())),
    "/all": system_info_check.SystemInfoCheck().get_all(),
    "/disk": system_info_check.SystemInfoCheck("disk").get_disk(),
    "/memory": system_info_check.SystemInfoCheck("memory").get_memory(),
}
