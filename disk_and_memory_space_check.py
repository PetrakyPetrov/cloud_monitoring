import re


class DiskAndMemorySpaceCheck:
    pass


if __name__ == "__main__":

    with open('/proc/meminfo') as f:
        meminfo = f.read()

    total_ram_KB = re.search(r'^MemTotal:\s+(\d+)', meminfo)
    free_ram_KB = re.search(r'^MemFree:\s+(\d+)', meminfo)
    available_ram_KB = re.search(r'^MemAvailable:\s+(\d+)', meminfo)
    swap_total_KB = re.search(r'^SwapTotal:\s+(\d+)', meminfo)
    swap_free_KB = re.search(r'^SwapFree:\s+(\d+)', meminfo)

    if total_ram_KB:
        total_ram_KB = int(total_ram_KB.groups()[0])

    if free_ram_KB:
        free_ram_KB = int(free_ram_KB.groups()[0])

    if available_ram_KB:
        available_ram_KB = int(available_ram_KB.groups()[0])

    if swap_total_KB:
        swap_total_KB = int(swap_total_KB.groups()[0])

    if swap_free_KB:
        swap_free_KB = int(swap_free_KB.groups()[0])

    print(total_ram_KB)
