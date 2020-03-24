from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    profil_picture = models.ImageField(upload_to='profil')
    cv_file = models.FileField(upload_to='file')
    position = models.ForeignKey(Position,on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname

    def delete(self, *args, **kwargs):
        self.profil_picture.delete()
        self.cv_file.delete()
        super().delete(*args, **kwargs)