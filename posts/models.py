# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.
class Article(models.Model):
	author=models.CharField(max_length=200,null=True,verbose_name='Name')
	title=models.CharField(max_length=200,null=True,verbose_name='Title')
	content=models.TextField(null=True,verbose_name='Content')
	likes=models.IntegerField(default=0)
	created_on=models.DateTimeField(default=timezone.now)
	
	class Meta:
		ordering = ('-likes',)

	def __unicode__(self):
		return self.title