from django.db import models


class djangoClasses(models.Model):
    title = models.CharField(max_length=50)
    coursenumber = models.IntegerField()
    instructor = models.CharField(max_length=50)
    duration = models.FloatField()

    objects = models.Manager()

    def __str__(self):
        return self.title


Course1 = djangoClasses(title='English', coursenumber=25, instructor='Matthew', duration=45)
Course1.save()

Course2 = djangoClasses(title='Math', coursenumber=15, instructor='June', duration=50)
Course2.save()

Course3 = djangoClasses(title='Biology', coursenumber=35, instructor='Connor', duration=55)
Course3.save()