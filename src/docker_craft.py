import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List

@dataclass
class Lab:
    title: str
    difficulty: str
    estimated_time: int
    content: str
    approved: bool = False

class DockerCraft:
    def __init__(self):
        self.pending_labs = []
        self.approved_labs = []

    def submit_lab(self, title: str, difficulty: str, estimated_time: int, content: str):
        lab = Lab(title, difficulty, estimated_time, content)
        self.pending_labs.append(lab)

    def approve_lab(self, title: str):
        for lab in self.pending_labs:
            if lab.title == title:
                lab.approved = True
                self.approved_labs.append(lab)
                self.pending_labs.remove(lab)
                return True
        return False

    def reject_lab(self, title: str):
        for lab in self.pending_labs:
            if lab.title == title:
                self.pending_labs.remove(lab)
                return True
        return False

    def get_approved_labs(self):
        return [lab for lab in self.approved_labs if lab.approved]

    def send_notification(self, title: str, approved: bool):
        print(f"Notification sent for {title}: {'Approved' if approved else 'Rejected'}")

    def review_labs(self):
        for lab in self.pending_labs:
            print(f"Reviewing lab: {lab.title}")

def main():
    craft = DockerCraft()
    craft.submit_lab("My Lab", "Easy", 30, "This is my lab")
    craft.approve_lab("My Lab")
    print(craft.get_approved_labs())

if __name__ == "__main__":
    main()
