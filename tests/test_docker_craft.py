from docker_craft import create_dockerized_app, generate_docker_compose, generate_github_actions_yaml
import json

def test_create_dockerized_app():
    app = create_dockerized_app("my_app", "my_image", 8080)
    assert app.name == "my_app"
    assert app.image == "my_image"
    assert app.port == 8080

def test_generate_docker_compose():
    app = create_dockerized_app("my_app", "my_image", 8080)
    docker_compose = generate_docker_compose(app)
    assert "version: '3'" in docker_compose
    assert "my_app:" in docker_compose
    assert "image: my_image" in docker_compose
    assert "ports:" in docker_compose
    assert "- \"8080:80\"" in docker_compose

def test_generate_github_actions_yaml():
    app = create_dockerized_app("my_app", "my_image", 8080)
    github_actions_yaml = generate_github_actions_yaml(app)
    assert "name: Build and deploy my_app" in github_actions_yaml
    assert "on:" in github_actions_yaml
    assert "push:" in github_actions_yaml
    assert "branches:" in github_actions_yaml
    assert "- main" in github_actions_yaml
    assert "jobs:" in github_actions_yaml
    assert "build-and-deploy:" in github_actions_yaml
    assert "runs-on: ubuntu-latest" in github_actions_yaml
    assert "steps:" in github_actions_yaml
    assert "name: Checkout code" in github_actions_yaml
    assert "uses: actions/checkout@v2" in github_actions_yaml
    assert "name: Login to Docker Hub" in github_actions_yaml
    assert "uses: docker/login-action@v1" in github_actions_yaml
    assert "name: Build and push Docker image" in github_actions_yaml
    assert "run: |" in github_actions_yaml
    assert "docker build -t my_image ." in github_actions_yaml
    assert "docker push my_image" in github_actions_yaml
    assert "name: Deploy to production" in github_actions_yaml
    assert "run: |" in github_actions_yaml
    assert "docker run -d -p 8080:80 my_image" in github_actions_yaml
