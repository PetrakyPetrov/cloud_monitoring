import re
import inspect
import os
import subprocess


class DiskAndMemorySpaceCheck:

    __memory = "Memory:\n"
    __disk = "Disk:\n"

    def __init__(self):

        free_output = subprocess.check_output("free")
        for line in free_output.splitlines():
            self.__memory += line.decode("utf-8") + "\n"

        df_output = subprocess.check_output("df")
        for line in df_output.splitlines():
            self.__disk += line.decode("utf-8") + "\n"

    def get_all(self, type="raw"):
        print(self.__memory)
        print(self.__disk)


if __name__ == "__main__":

    system_info = DiskAndMemorySpaceCheck()
    system_info.get_all()
