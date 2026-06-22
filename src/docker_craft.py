import argparse
import json
import subprocess
from dataclasses import dataclass
from urllib.parse import urlparse

@dataclass
class Project:
    id: str
    url: str

def validate_docker_install():
    try:
        subprocess.check_output(['docker', 'ps'])
        return True
    except FileNotFoundError:
        return False
    except subprocess.CalledProcessError:
        return False

def clone_repo(project_id):
    try:
        subprocess.check_output(['git', 'clone', f'https://github.com/{project_id}.git'])
        return True
    except subprocess.CalledProcessError:
        return False

def start_containers(project_id):
    try:
        subprocess.check_output(['docker-compose', 'up', '-d'], cwd=project_id)
        return True
    except subprocess.CalledProcessError:
        return False
    except FileNotFoundError:
        return False

def init_project(project_id):
    if not validate_docker_install():
        raise RuntimeError('Docker is not running')
    if not clone_repo(project_id):
        raise RuntimeError('Failed to clone repository')
    if not start_containers(project_id):
        raise RuntimeError('Failed to start containers')
    return Project(id=project_id, url=f'http://localhost:8080/{project_id}')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['init'])
    parser.add_argument('project_id')
    args = parser.parse_args()
    if args.command == 'init':
        try:
            project = init_project(args.project_id)
            print(f'Project initialized successfully. Access URL: {project.url}')
        except RuntimeError as e:
            print(f'Error: {e}')

if __name__ == '__main__':
    main()
