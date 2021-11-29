from django.db import models

# Create your models here.
class TshirtProperty(models.Model):
    title =models.CharField(max_length=30, null=False)
    slug= models.CharField(max_length=30, null=False, unique= True)

    def __str__(self):
        return self.title
    class Meta:
        abstract= True
class Occasion(TshirtProperty):
    pass
class IdealFor(TshirtProperty): 
    pass
class Sleeve(TshirtProperty):
    pass
class Brand(TshirtProperty):
    pass
class Necktype(TshirtProperty):
    pass
class Colour(TshirtProperty):
    pass
class Tshirt(models.Model):
    name = models.CharField(max_length=50, null= False)
    description = models.CharField(max_length=500, null=True)
    discount= models.IntegerField(default=0)
    image= models.ImageField(upload_to="upload/images/", null=False)
    occasion= models.ForeignKey(Occasion, on_delete=models.CASCADE)
    brand= models.ForeignKey(Brand, on_delete=models.CASCADE)
    sleeve= models.ForeignKey(Sleeve, on_delete=models.CASCADE)
    neck_type= models.ForeignKey(Necktype, on_delete=models.CASCADE)
    ideal_for= models.ForeignKey(IdealFor, on_delete=models.CASCADE)
    colour= models.ForeignKey(Colour, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class SizeVarient(models.Model):
    SIZES= (("S","SMALL"),("M","MEDIUM"),("L","LARGE"),("XL","EXTRA LARGE"),("XXL","EXTRA EXTRA LARGE"))
    price=models.IntegerField(null=False)
    tshirt=models.ForeignKey(Tshirt,on_delete=models.CASCADE)
    size=models.CharField(choices=SIZES, max_length=5)