from django.db import models



class pesticidelist(models.Model):
    dname = models.CharField(max_length=100)
    pname = models.CharField(max_length=100)
    ddesc = models.CharField(max_length=500)


class Feedback(models.Model):
    name = models.CharField(max_length=255)
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    