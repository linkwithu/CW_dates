from django.db import models
from django.conf import settings
from django.utils import timezone

class Work_week(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    workers=(('Kristina','Kristina'),('Lena','Lena'),('Milana','Milana'),('Violetta','Violetta'),('Andrey','Andrey'),
             ('Syun','Syun'),('Inna','Inna'),('Kirill','Kirill'))
    day_week=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    title=models.CharField(max_length=200)
    MondayGal=models.CharField(max_length=8,choices=workers)
    TuesdayGal=models.CharField(max_length=8,choices=workers)
    WednesdayGal=models.CharField(max_length=8,choices=workers)
    ThursdayGal=models.CharField(max_length=8,choices=workers)
    FridayGal=models.CharField(max_length=8,choices=workers)
    SaturdayGal=models.CharField(max_length=8,choices=workers)
    SundayGal=models.CharField(max_length=8,choices=workers)
    MondayVos=models.CharField(max_length=8,choices=workers)
    TuesdayVos=models.CharField(max_length=8,choices=workers)
    WednesdayVos=models.CharField(max_length=8,choices=workers)
    ThursdayVos=models.CharField(max_length=8,choices=workers)
    FridayVos=models.CharField(max_length=8,choices=workers)
    SaturdayVos=models.CharField(max_length=8,choices=workers)
    SundayVos=models.CharField(max_length=8,choices=workers)
    created_date = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_at = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title
