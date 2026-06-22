import pytest
from unittest.mock import patch
from docker_craft import validate_docker_install, clone_repo, start_containers, init_project, Project

def test_validate_docker_install():
    with patch('subprocess.check_output') as mock_check_output:
        mock_check_output.return_value = b'output'
        assert validate_docker_install() == True

def test_clone_repo():
    with patch('subprocess.check_output') as mock_check_output:
        mock_check_output.return_value = b'output'
        assert clone_repo('test-project') == True

def test_start_containers():
    with patch('subprocess.check_output') as mock_check_output:
        mock_check_output.return_value = b'output'
        assert start_containers('test-project') == True

def test_init_project():
    with patch('docker_craft.validate_docker_install') as mock_validate_docker_install:
        mock_validate_docker_install.return_value = True
        with patch('docker_craft.clone_repo') as mock_clone_repo:
            mock_clone_repo.return_value = True
            with patch('docker_craft.start_containers') as mock_start_containers:
                mock_start_containers.return_value = True
                project = init_project('test-project')
                assert isinstance(project, Project)
                assert project.id == 'test-project'
                assert project.url == 'http://localhost:8080/test-project'

def test_init_project_docker_not_running():
    with patch('docker_craft.validate_docker_install') as mock_validate_docker_install:
        mock_validate_docker_install.return_value = False
        with pytest.raises(RuntimeError):
            init_project('test-project')

def test_init_project_clone_repo_failure():
    with patch('docker_craft.validate_docker_install') as mock_validate_docker_install:
        mock_validate_docker_install.return_value = True
        with patch('docker_craft.clone_repo') as mock_clone_repo:
            mock_clone_repo.return_value = False
            with pytest.raises(RuntimeError):
                init_project('non-existent-project')

def test_init_project_start_containers_failure():
    with patch('docker_craft.validate_docker_install') as mock_validate_docker_install:
        mock_validate_docker_install.return_value = True
        with patch('docker_craft.clone_repo') as mock_clone_repo:
            mock_clone_repo.return_value = True
            with patch('docker_craft.start_containers') as mock_start_containers:
                mock_start_containers.return_value = False
                with pytest.raises(RuntimeError):
                    init_project('test-project')
