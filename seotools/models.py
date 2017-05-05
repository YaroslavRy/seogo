from django.db import models


class Metatags(models.Model):
	page_uri = models.CharField(max_length=128)
	title_text = models.CharField(max_length=128, default='')
	description_text = models.CharField(max_length=256, default='')
	def __str__(self):
		return self.page_uri
