from django.db import models

class Zombie(models.Model):
	name = models.CharField(max_length=50)
	cemetery = models.CharField(max_length=25)
	date_death = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return 'Zombie: %s - %s' % (self.id,self.name)


class Tweet(models.Model):
	zombie = models.ForeignKey("Zombie",related_name='tweet')
	status = models.CharField(max_length=140)
	created_t = models.DateTimeField(auto_now_add=True)