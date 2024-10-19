from django.contrib import admin

from s3_upload import models

admin.site.register(models.Document)
admin.site.register(models.Person)
