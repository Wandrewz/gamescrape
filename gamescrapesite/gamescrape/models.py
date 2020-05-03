from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    cover = models.ImageField(upload_to='images/')
    amazonurl = models.URLField(max_length=200)
    amazonprice = models.DecimalField(max_digits=5, decimal_places=2, default=100.00)
    walmarturl = models.URLField(max_length=200)
    walmartprice = models.DecimalField(max_digits=5, decimal_places=2, default=100.00)
    lowestprice = models.DecimalField(max_digits=5, decimal_places=2, default=100.00)
    loweststore = models.CharField(max_length=10, default='None')
    lowesturl = models.URLField(max_length=200, default='amazon.com')
    historiclow = models.DecimalField(max_digits=5, decimal_places=2, default=100.00)

    def __str__(self):
        return self.title
