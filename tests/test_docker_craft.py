import pytest
from src.docker_craft import DockerCraft, Lab

def test_submit_lab():
    craft = DockerCraft()
    craft.submit_lab("My Lab", "Easy", 30, "This is my lab")
    assert len(craft.pending_labs) == 1

def test_approve_lab():
    craft = DockerCraft()
    craft.submit_lab("My Lab", "Easy", 30, "This is my lab")
    craft.approve_lab("My Lab")
    assert len(craft.approved_labs) == 1
    assert len(craft.pending_labs) == 0

def test_reject_lab():
    craft = DockerCraft()
    craft.submit_lab("My Lab", "Easy", 30, "This is my lab")
    craft.reject_lab("My Lab")
    assert len(craft.pending_labs) == 0

def test_get_approved_labs():
    craft = DockerCraft()
    craft.submit_lab("My Lab", "Easy", 30, "This is my lab")
    craft.approve_lab("My Lab")
    approved_labs = craft.get_approved_labs()
    assert len(approved_labs) == 1
    assert approved_labs[0].title == "My Lab"

def test_send_notification():
    craft = DockerCraft()
    craft.submit_lab("My Lab", "Easy", 30, "This is my lab")
    craft.approve_lab("My Lab")
    craft.send_notification("My Lab", True)
    # No assertion, just checking that it runs without error

def test_review_labs():
    craft = DockerCraft()
    craft.submit_lab("My Lab", "Easy", 30, "This is my lab")
    craft.review_labs()
    # No assertion, just checking that it runs without error
