import subprocess


class SystemInfoCheck:

    __memory = "{section_name}:\n".format(section_name="Memory")
    __disk = "{section_name}:\n".format(section_name="Disk")
    __cpu = "{section_name}:\n".format(section_name="CPU")

    def __init__(self, sys_info_type="all"):

        if sys_info_type == "memory" or sys_info_type == "all":
            free_output = subprocess.check_output("free -h")
            for line in free_output.splitlines():
                self.__memory += "{row}\n".format(row=line.decode("utf-8"))

        if sys_info_type == "disk" or sys_info_type == "all":
            df_output = subprocess.check_output("df -h")
            for line in df_output.splitlines():
                self.__disk += "{row}\n".format(row=line.decode("utf-8"))

        if sys_info_type == "cpu" or sys_info_type == "all":
            df_output = subprocess.check_output("lscpu")
            for line in df_output.splitlines():
                self.__cpu += "{row}\n".format(row=line.decode("utf-8"))

    def get_all(self, type="raw"):
        return "{mem_info}\n{disk_info}\n{cpu_info}".format(
            mem_info=self.__memory,
            disk_info=self.__disk,
            cpu_info=self.__cpu
        )

    def get_memory(self, type="raw"):
        return self.__memory

    def get_disk(self, type="raw"):
        return self.__disk

    def get_cpu(self, type="raw"):
        return self.__cpu
