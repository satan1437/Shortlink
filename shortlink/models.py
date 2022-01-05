import base64
import uuid

from django.db import models
from django.contrib.auth.models import User

HOST_NAME = 'https://shrlnker.herokuapp.com/'


class CreateURL(models.Model):
	url = models.URLField('URL')
	url_hash = models.CharField('Хэш', max_length=10, unique=True, db_index=True)
	shorted_url = models.CharField('Сокращённая ссылка', max_length=256, blank=True, null=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель ссылки')

	def save(self, *args, **kwargs):
		self.url_hash = self.generate_hash()
		self.shorted_url = self.create_short_url()
		super(CreateURL, self).save(*args, **kwargs)

	def generate_hash(self):
		new_hash = base64.urlsafe_b64encode(uuid.uuid1().bytes)[:10]
		is_valid_data = CreateURL.objects.filter(url_hash=new_hash)

		while is_valid_data:
			new_hash = base64.urlsafe_b64encode(uuid.uuid1().bytes)[:10]
			is_valid_data = CreateURL.objects.filter(url_hash=new_hash)
			continue

		complete_hash = new_hash.decode('utf-8')
		return complete_hash

	def create_short_url(self):
		return HOST_NAME + self.url_hash

	def __str__(self):
		return f'{self.owner} | {self.url[:15]}'

	class Meta:
		verbose_name = 'Ссылка'
		verbose_name_plural = 'Ссылки'
