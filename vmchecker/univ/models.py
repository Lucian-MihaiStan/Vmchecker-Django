import uuid
from django.db import models
from django.urls import reverse


# Create your models here.


class Homework(models.Model):
    homework_name = models.CharField(max_length=200)
    text_homework = models.TextField(blank=True)

    class Meta:
        ordering = ['homework_name']

    def get_absolute_url(self):
        return reverse('homework-detail', args=[str(self.id)])

    def __str__(self):
        return "\n" + str(self.homework_name) + " with text " + str(self.text_homework) + "\n"


class HomeworkInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular homework")
    homework = models.ForeignKey('Homework', on_delete=models.RESTRICT)


class Subject(models.Model):
    subject_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    homework_list = models.ManyToManyField(Homework)

    class Meta:
        ordering = ['subject_name']

    def get_absolute_url(self):
        return reverse('subject-detail', args=[str(self.id)])

    def __str__(self):
        return "Subject \n" + str(self.subject_name) + "\nWith description: \n" + str(self.description)


class SubjectInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular subject")
    subject = models.ForeignKey('Subject', on_delete=models.RESTRICT)


class Year(models.Model):
    year_count = models.CharField(max_length=200)
    subjects = models.ManyToManyField(Subject)
    year_introduction = models.CharField(max_length=200)

    def __str__(self):
        return str(self.year_count)

    def getId(self):
        return str(self.year_count[:1])

    def getName(self):
        return str(self.year_count[2:])

    def get_absolute_url(self):
        return reverse('year-detail', args=[str(self.id)])

    def getFullUniversityYearName(self):
        year = self.getId()
        name = self.getName()
        dictionary = {
            'CTI': 'Automatica si calculatoare',
            'IS': 'Ingineria sistemelor',
            'IE': 'Inginerie electrica'
        }
        return dictionary.get(name) + ' Year ' + year


class YearInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular year")
    year = models.ForeignKey('Year', on_delete=models.RESTRICT)


class Univ(models.Model):
    univ_name = models.CharField(max_length=50)
    years = models.ManyToManyField(Year)

    class Meta:
        ordering = ['univ_name']

    def __str__(self):
        return "University " + str(self.univ_name)

    def get_absolute_url(self):
        return reverse('university-detail', args=[str(self.id)])


class UnivInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular univ")
    univ = models.ForeignKey('Univ', on_delete=models.RESTRICT)

    def __str__(self):
        return '{0} ({1})'.format(self.id, self.univ.univ_name)
