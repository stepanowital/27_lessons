from django.db import models
from uuid import uuid4


class Feedback(models.Model):
    STATUS = [(1, "yes"), (2, "no")]
    correlation_id = models.UUIDField(default=uuid4, editable=False, unique=True)
    user_feedback = models.IntegerField(null=True, choices=STATUS)
    user_feedback_timestamp = models.DateTimeField(auto_now_add=True, null=True)
    closed = models.BooleanField(default=False)


class Destination(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    to_name = models.CharField(max_length=100, null=True, blank=True)
    flag = models.CharField(max_length=10, null=True, blank=True)
    visa_id = models.PositiveSmallIntegerField(null=True, blank=True)
    covid_status = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
