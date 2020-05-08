import datetime
from django.utils import timezone

from django.db import models


class Log(models.Model):
    time_stamp = models.TextField(blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    function = models.TextField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'Log'


class Genre(models.Model):
    genreid = models.AutoField(db_column='GenreId', primary_key=True)
    name = models.TextField(db_column='Name', blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'Genre'


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


    def __str__(self):
        return self.question_text


    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


    def __str__(self):
        return self.choice_text
