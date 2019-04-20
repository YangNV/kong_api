#!venv/bin/python
import requests


def build_service(container_info: tuple, port=8080) -> str:
    payload = {
        "name": container_info[0],
        "host": container_info[1],
        "protocol": "http",
        "port": port,
        # "path": r"/api{0}".format(container_info[0])
    }
    requests_url = "http://localhost:8001/services{0}".format(container_info[0])

    result = requests.put(url=requests_url, data=payload)
    if result.json()["id"]:
        return result.json()["id"]
    else:
        return build_service(container_info=container_info, port=port)


def build_route(container_info: tuple, host: str, id: str):
    payload = {
        "name": container_info[0],
        "hosts": host,
        "paths": r"/api{0}".format(container_info[0]),
        "service.id": id
    }
    requests_url = "http://localhost:8001/routes{0}".format(container_info[0])

    result = requests.put(url=requests_url, data=payload)
    return result.json()


if __name__ == '__main__':
    id = build_service(('/qq', 'www.baidu.com'), port=80)
    print(build_route(('/qq', 'www.baidu.com'), "me.com", id))

