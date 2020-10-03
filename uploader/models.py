from django.db import models
from django.core.exceptions import ValidationError

def file_size(value): # add this to some file where you can import it from
    limit = 30 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 30 MiB.')

class FileUpload(models.Model):
	file = models.FileField(validators=[file_size])
	file_name = models.CharField(max_length=500)
	description = models.CharField(max_length=500, blank=True, null=True)
	uploaded_at = models.DateTimeField()
	expired_at = models.DateTimeField()