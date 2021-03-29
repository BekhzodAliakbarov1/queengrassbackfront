from django.db import models

# First Model
class Product(models.Model):
    TypeOfProducts = (
        ('Газоны Queens Grass','Газоны Queens Grass'),
        ('Dennis UK','Dennis UK'),
        ('Sisis','Sisis'),
        ('Trilo','Trilo'),
        ('Vredo','Vredo'),
        ('Redexim','Redexim'),
        ('Harrod UK','Harrod UK'),
        ('Compact tractors','Compact tractors'),
        ('Hunter','Hunter'),
        ('Другое','Другое')
    )
    nameOfProduct = models.CharField(max_length=200, blank=True, null=True)
    typeOfProduct = models.CharField(default='Другое',max_length=200, null=True,choices=TypeOfProducts)
    image = models.ImageField(null=True, blank=True)
    titleFirst = models.CharField(max_length=200, blank=True, null=True)
    paragraphFirst = models.CharField(max_length=1000, blank=True, null=True)
    titleSecond = models.CharField(max_length=200, blank=True, null=True, default='It is not compulsory')
    paragraphSecond = models.CharField(max_length=1000, blank=True, null=True, default='It is not compulsory')

    def __str__(self):
        return self.typeOfProduct
































# #Second Model
# class Car(models.Model):
#     name = models.CharField(max_length=200, blank=True, null=True)
#     number = models.IntegerField( blank=True, null=True)
#     image = models.ImageField(null=True, blank=True)
#     titleFirst = models.CharField(max_length=200, blank=True, null=True)
#     paragraphFirst = models.CharField(max_length=1000, blank=True, null=True)
#     titleSecond = models.CharField(max_length=200, blank=True, null=True, default='It is not compulsory')
#     paragraphSecond = models.CharField(max_length=1000, blank=True, null=True, default='It is not compulsory')


#     def __str__(self):
#         return self.name

# #third Model
# class Door(models.Model):
#     name = models.CharField(max_length=200, blank=True, null=True)
#     number = models.IntegerField( blank=True, null=True)
#     image = models.ImageField(null=True, blank=True)
#     titleFirst = models.CharField(max_length=200, blank=True, null=True)
#     paragraphFirst = models.CharField(max_length=1000, blank=True, null=True)
#     titleSecond = models.CharField(max_length=200, blank=True, null=True, default='It is not compulsory')
#     paragraphSecond = models.CharField(max_length=1000, blank=True, null=True,default='It is not compulsory')


#     def __str__(self):
#         return self.name