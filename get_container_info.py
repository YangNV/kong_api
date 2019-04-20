#!venv/bin/python
import os


def get_container_info() -> list:
    ls = os.popen(
        r"docker inspect --format='{{.Name}} {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps -q)")
    ip_list = []
    for line in ls.readlines():
        name, ip = line.strip().split(" ")
        if name == "/kong" or name == "/kong-database":
            continue
        ip_list.append((name, ip))
    return ip_list


if __name__ == '__main__':
    print(get_container_info())
