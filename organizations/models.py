from django.db import models
from locations.models import Location
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Category(models.Model):
    """
    This model will hold the different categories of organizations that we can register. ie Finance, Medical etc.
    An organization will be able to register in one or more categories.
    
    """
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return "{}".format(self.name)


class Product(models.Model):
    """
    This model will hold the different types of services or products that can be provided by different organizations.
    An organization will be able to provide one or more services.

    """
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = _("Service_Product")
        verbose_name_plural = _("Services_Products")

    def __str__(self):
        return "{}".format(self.name)


class Organization(models.Model):
    name = models.CharField(max_length=128)
    Category = models.ManyToManyField(Category, related_name="categories")
    products_services = models.ManyToManyField(Product, related_name="products")
    description = models.TextField()

    def __str__(self):
        return "{}".format(self.name)


class OrganizationBranch(models.Model):
    """
    The same organization can have one or more branches in different locations.
    
    """
    name = models.CharField(max_length=128)
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING, related_name="branches")
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _("Branch")
        verbose_name_plural = _("Organization Branches")

    def __str__(self):
        return "{} - {} ({})".format(self.organization, self.name, self.location.name)


class Contact(models.Model):
    """
    An organization can have one or more contacts or contact persons attached to a branch.
    
    """
    name = models.CharField(max_length=128)
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING, related_name="contacts")
    organization_branch = models.ForeignKey(OrganizationBranch, on_delete=models.CASCADE)
    phone = models.CharField(max_length=128)

    def __str__(self):
        return "{} ({})".format(self.name, self.phone)