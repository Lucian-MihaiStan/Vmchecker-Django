import uuid
from django.db import models


# Create your models here.


class Homework(models.Model):
    homework_name = models.CharField(max_length=200)
    text_homework = models.TextField(blank=True)

    def __str__(self):
        return "\n" + str(self.homework_name) + " with text " + str(self.text_homework) + "\n"


class HomeworkInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular homework")
    homework = models.ForeignKey('Homework', on_delete=models.RESTRICT)


class Subject(models.Model):
    subject_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    homework_list = models.ManyToManyField(Homework)
    
    def __str__(self):
        return "Subject \n" + str(self.subject_name) + "\nWith description: \n" + str(self.description)


class SubjectInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular subject")
    subject = models.ForeignKey('Subject', on_delete=models.RESTRICT)


class Year(models.Model):
    year_count = models.CharField(max_length=200)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return str(self.year_count)


class YearInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular year")
    year = models.ForeignKey('Year', on_delete=models.RESTRICT)


class Univ(models.Model):
    univ_name = models.CharField(max_length=30)
    years = models.ManyToManyField(Year)

    class Meta:
        ordering = ['univ_name']

    def __str__(self):
        return "University " + str(self.univ_name)


class UnivInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular univ")
    univ = models.ForeignKey('Univ', on_delete=models.RESTRICT)

    def __str__(self):
        return '{0} ({1})'.format(self.id, self.univ.univ_name)
