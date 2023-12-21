from django.db import models
# Create your models here.
class BookModel(models.Model):
    Title = models.CharField(max_length=50)
    Author = models.ForeignKey("AuthorModel", on_delete=models.CASCADE , blank = False)
    Publication_Year = models.IntegerField()
    ISBN = models.CharField(max_length=50,unique=True)
    Price = models.DecimalField(max_digits=8, decimal_places=3)

    def __str__(self):
        return self.Title
class AuthorModel(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=200)
    def __str__(self):
        return self.First_Name