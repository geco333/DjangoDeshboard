# Generated by Django 3.0.6 on 2020-05-07 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('genreid', models.AutoField(db_column='GenreId', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
            ],
            options={
                'db_table': 'Genre',
                'managed': False,
            },
        ),
    ]
