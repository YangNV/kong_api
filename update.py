#!venv/bin/python
from get_container_info import get_container_info
import buildPayload

if __name__ == '__main__':
    host = "127.0.0.1"
    containers_info = get_container_info()
    for container in containers_info:
        service_id = buildPayload.build_service(container_info=container)
        buildPayload.build_route(container_info=container, host=host, id=service_id)
    print("Done")
