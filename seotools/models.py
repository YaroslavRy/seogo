from django.db import models


class Title(models.Model):
	title_text = models.CharField(max_length=128)


class Description(models.Model):
	description_text = models.CharField(max_length=256)