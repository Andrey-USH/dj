from django.db import models
from django.urls import reverse


class Staff(models.Model):
    firstname = models.CharField("Имя", max_length=100)
    lastname = models.CharField("Фамилия", max_length=100)
    patronymic = models.CharField("Отчество", max_length=100)
    dateOfBirth = models.DateField("Дата рождения", auto_now_add=False)
    startDateWork = models.DateField("дата начала работы", auto_now_add=False, blank=True)
    photo = models.ImageField(upload_to='photo/')
    department = models.ForeignKey('Department', verbose_name='отдел', on_delete=models.PROTECT, null=True)

    def get_absolute_url(self):
        return reverse("get_staff", kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.lastname}"


class Department(models.Model):
    name = models.CharField("отдел", max_length=100, db_index=True)

    def get_absolute_url(self):
        return reverse("department", kwargs={'department_id': self.pk})

    def __str__(self):
        return f"{self.name}"
