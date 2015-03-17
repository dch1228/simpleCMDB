import django.db

# Create your models here.
class UserInfo(django.db.models.Model):
	uid = django.db.models.AutoField(primary_key=True)
	username = django.db.models.CharField(max_length=10)
	realName = django.db.models.CharField(max_length=10)
	gender = django.db.models.NullBooleanField()
	email = django.db.models.EmailField(max_length=128)

	def __unicode__(self):
		return self.username