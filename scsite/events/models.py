from django.db import models
from datetime import time
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset() \
            .filter(status=Event.Status.PUBLISHED)


class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    zip = models.IntegerField()
    directions = models.URLField(max_length=200, default="https://www.google.com/maps")

    def __str__(self):
        return f"{self.name}"


class Event(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    class Type(models.TextChoices):
        SKILLS = 'SC', 'Skills Clinic'
        GROUP = 'GR', 'Group Ride'
        OTHER = 'OT', 'Other'

    class SkillLevel(models.TextChoices):
        ALL = 'All Levels'
        BEGIN = 'Beginner'
        INTER = 'Intermediate'
        ADVANCED = 'Advanced'
        EXPERT = 'Expert'

    title = models.CharField(max_length=200)
    event_image = models.ImageField(null=True, blank=True, upload_to="images/")
    slug = models.SlugField(max_length=250,
                            unique_for_date='date')
    skill_level = models.CharField(max_length=20,
                                   choices=SkillLevel.choices)
    type = models.CharField(max_length=2,
                            choices=Type.choices)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    end_time = models.TimeField(default=time(10))
    price = models.DecimalField(max_digits=10, decimal_places=2, default=(0))
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    class Meta:
        ordering = ['date']
        indexes = [
            models.Index(fields=['date']),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('events:event_detail',
                       args=[self.date.year,
                             self.date.month,
                             self.date.day,
                             self.slug])
