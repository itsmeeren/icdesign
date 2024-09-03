
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class EventImage(models.Model):
    event = models.ForeignKey(Event, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_images/')

    def __str__(self):
        return f"Image for {self.event.title}"
