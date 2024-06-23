from django.db import models

# Create your models here.
class employee(models.Model):
    name=models.CharField(max_length=100)
    emp_id=models.IntegerField()
    email=models.EmailField()
    salary=models.IntegerField()
    photo = models.ImageField(upload_to='images')
    def __str__(self):
        return self.name