# Docker Container Management

## Table of Contents

- [List all running processes in a container](#list-all-running-processes-in-a-container)
- [Exit the Container without terminating it](#exit-the-container-without-terminating-it)
- [List All Running Containers](#list-all-running-containers)
- [Attaching to a Running Container](#attaching-to-a-running-container)
- [Stop the Container](#stop-the-container)
- [List All Containers, Even Those in a Stopped State](#list-all-containers-even-those-in-a-stopped-state)
- [Remove (Kill) a Container](#remove-kill-a-container)

---

## List all running processes in a container

- **Command**: `ps -elf`
- **Explanation**: Use this command inside a Docker container to view all running processes. It provides details like process ID, user, and the command that started each process.
- **Example**:
  ```bash
  ps -elf
  ```

## Exit the Container without terminating it

- **Action**: Press `Ctrl-P` then `Ctrl-Q`.
- **Explanation**: This key combination allows you to detach from a container's terminal without stopping the container. The container continues to run in the background.

## List All Running Containers

- **Command**: `docker ps`
- **Explanation**: This command lists all currently running containers, displaying information like container ID, image, command, and uptime.
- **Example**:
  ```bash
  docker ps
  ```

## Attaching to a Running Container

- **Command**: `docker exec -it container_name bash`
- **Explanation**: Use this command to start an interactive Bash shell session inside a running container. This is useful for debugging or managing the container.
- **Example**:
  ```bash
  docker exec -it container_name bash
  ```

## Stop the Container

- **Command**: `docker stop container_name`
- **Explanation**: This command stops a running container gracefully, allowing it to shut down cleanly.
- **Example**:
  ```bash
  docker stop container_name
  ```

## List All Containers, Even Those in a Stopped State

- **Command**: `docker ps -a`
- **Explanation**: This command lists all containers, whether they are running, stopped, or exited.
- **Example**:
  ```bash
  docker ps -a
  ```

## Remove (Kill) a Container

- **Command**: `docker rm container_name`
- **Explanation**: This command removes a container from the system. Make sure the container is stopped before attempting to remove it.
- **Example**:
  ```bash
  docker rm container_name
  ```

---

This guide provides a basic overview of managing Docker containers. For more advanced usage, refer to the official Docker documentation.
