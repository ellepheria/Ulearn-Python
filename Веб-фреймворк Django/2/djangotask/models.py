from django.db import models


class SiteUser(models.Model):
    first_name = models.CharField("Имя", max_length=255)
    last_name = models.CharField("Фамилия", max_length=255)

    def get_name(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        db_table = "site_users"


class Vacancy(models.Model):
    name = models.TextField()
    salary = models.TextField()
    area_name = models.TextField()
    published_at = models.TextField()

    class Meta:
        db_table = "vacancies"
