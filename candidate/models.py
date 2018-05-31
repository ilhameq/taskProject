from django.db import models
from enum import Enum

class Candidate(models.Model):



    class Status(Enum):
        a = "available"
        p = "pending"
        r = "rejected"

    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=[(tag.value, tag) for tag in Status])
