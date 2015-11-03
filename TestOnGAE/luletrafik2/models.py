from django.db import models
from django.contrib.auth.models import User


DEFAULT_GUESTBOOK_NAME = 'default_guestbook'

# We set a parent key on the 'Greetings' to ensure that they are all in the same
# entity group. Queries across the single entity group will be consistent.
# However, the write rate should be limited to ~1/second.


class Greeting(models.Model):
    author = models.ForeignKey(User, null=True, blank=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)