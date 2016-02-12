from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserDetail(models.Model):
	user = models.ForeignKey(User)
	phone_number = models.BigIntegerField(null= False)

	def __unicode__(self):
		return self.user.username



