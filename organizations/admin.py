from django.contrib import admin
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin, ExportActionModelAdmin
from import_export.widgets import ForeignKeyWidget

from . import models


admin.site.site_header = "ValueMat Administration"
admin.site.site_title = "ValueMat Administration"
admin.site.index_title = ""

#TODO make it possible for organization data to be imported.

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Product)
class ProductServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

@admin.register(models.OrganizationBranch)
class OrganizationBranchAdmin(admin.ModelAdmin):
    pass