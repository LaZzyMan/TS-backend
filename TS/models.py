from django.contrib.gis.db import models
# Create your models here.


class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=50, verbose_name='User ID')
    password = models.CharField(max_length=100)
    name = models.CharField(verbose_name='Real Name', max_length=50)
    email = models.CharField(verbose_name='Email Address', max_length=100)

    def __str__(self):
        return self.name


class POI(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='POI Name', max_length=100)
    type = models.CharField(verbose_name='POI Type', max_length=100)
    address = models.CharField(verbose_name='POI Address', max_length=200)
    location = models.PointField(srid=4326, verbose_name='位置', null=True)
    picture = models.ImageField(verbose_name='POI Picture', upload_to='poi/')

    def __str__(self):
        return self.name


class Trace(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User',
                             db_index=True, related_name='userTrace')
    points = models.TextField(verbose_name='Points of trace')
    start_time = models.DateTimeField(verbose_name='Start time of trace')
    end_time = models.DateTimeField(verbose_name='End time of trace')

    def __str__(self):
        return self.points


class StayPoint(models.Model):
    id = models.BigAutoField(primary_key=True)
    location = models.ForeignKey(POI, verbose_name='POI of Stay Point', related_name='stayPointLoc',
                                 on_delete=models.CASCADE, db_index=True)
    start_time = models.DateTimeField(verbose_name='Start time of stay')
    end_time = models.DateTimeField(verbose_name='End time of stay')

    def __str__(self):
        return self.location.name
