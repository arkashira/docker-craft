import json
from dataclasses import dataclass
from argparse import ArgumentParser

@dataclass
class DockerizedApp:
    name: str
    image: str
    port: int

def create_dockerized_app(name: str, image: str, port: int) -> DockerizedApp:
    return DockerizedApp(name, image, port)

def generate_docker_compose(app: DockerizedApp) -> str:
    return f"""
version: '3'
services:
  {app.name}:
    image: {app.image}
    ports:
      - "{app.port}:80"
"""

def generate_github_actions_yaml(app: DockerizedApp) -> str:
    return f"""
name: Build and deploy {app.name}
on:
  push:
    branches:
      - main
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
      - name: Login to Docker Hub
        uses: docker/login-action@v1
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}
      - name: Build and push Docker image
        run: |
          docker build -t {app.image} .
          docker push {app.image}
      - name: Deploy to production
        run: |
          docker run -d -p {app.port}:80 {app.image}
"""

def main():
    parser = ArgumentParser()
    parser.add_argument("--name", help="Name of the Dockerized app")
    parser.add_argument("--image", help="Docker image name")
    parser.add_argument("--port", type=int, help="Port number")
    args = parser.parse_args()

    app = create_dockerized_app(args.name, args.image, args.port)
    print(generate_docker_compose(app))
    print(generate_github_actions_yaml(app))

if __name__ == "__main__":
    main()
