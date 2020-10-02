from django.db import models

# Create your models here.
class FileUpload(models.Model):
	file = models.FileField()
	file_name = models.CharField(max_length=500)
	description = models.CharField(max_length=500, blank=True, null=True)
	uploaded_at = models.DateTimeField()
	expired_at = models.DateTimeField()