from unicodedata import category
from django.db import models


class Proposal(models.Model):
    name = models.CharField(max_length=255, null=False,
                            blank=False, verbose_name="Name")
    email = models.EmailField(null=False, blank=False, verbose_name="Email")
    phone = models.CharField(max_length=255, blank=False,
                             verbose_name="Phone Number")
    proposalText = models.TextField(
        null=False, blank=False, verbose_name="Requested Proposal")

    def __str__(self):
        return self.name


class PortfolioShowcase(models.Model):
    aboutProduct = models.TextField(
        null=False, blank=False, verbose_name="About Product")
    link = models.URLField(blank=False, null=False,
                           verbose_name="Portfolio Link")
    picture = models.ImageField(
        upload_to='portfolio-showcase', blank=False, null=False, verbose_name="Image")

    def __str__(self):
        return self.link


class PortfolioProduct(models.Model):
    # category = models.CharField(
    #     max_length=255, null=False, blank=False, verbose_name="Category", choices=(('Design', 'Design'), ('Development',
    #   'Development'), ('Design & Development', 'Design & Development'), ('Growth', 'Growth')))
    technology = models.CharField(max_length=255, null=False, blank=False)
    about = models.TextField(
        null=False, blank=False, verbose_name="About Product")
    portfolio = models.ForeignKey(
        PortfolioShowcase, related_name='portfolio', on_delete=models.CASCADE)

    # def __str__(self):
    # return self.category


class Services(models.Model):
    category = models.CharField(max_length=256, choices=(('Design', 'Design'), ('Development',
                                                                                'Development'), ('Design & Development', 'Design & Development'), ('Growth', 'Growth')), null=False, blank=False)
    title = models.CharField(max_length=256, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class SubServices(models.Model):
    Services = models.ForeignKey(
        Services, related_name='sub', on_delete=models.CASCADE)
    portfolio = models.ForeignKey(
        PortfolioProduct, related_name='sub', on_delete=models.CASCADE)
    portfolio_showcase = models.ForeignKey(
        PortfolioShowcase, related_name='sub', on_delete=models.CASCADE)
