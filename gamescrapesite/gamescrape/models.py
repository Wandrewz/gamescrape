from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    cover = models.ImageField(upload_to='images/')
    amazonurl = models.URLField(max_length=200)
    amazonprice = models.DecimalField(max_digits=5, decimal_places=2)
    walmarturl = models.URLField(max_length=200)
    walmartprice = models.DecimalField(max_digits=5, decimal_places=2)
    lowestprice = models.DecimalField(max_digits=5, decimal_places=2)
    loweststore = models.CharField(max_length=10)
    lowesturl = models.URLField(max_length=200)
    historiclow = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title
