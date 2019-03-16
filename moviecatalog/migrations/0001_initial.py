# Generated by Django 2.1.5 on 2019-03-15 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a movie genre', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('director', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('summary', models.TextField(help_text='Enter a brief description of the movie', max_length=1000)),
                ('genre', models.ManyToManyField(help_text='Select a genre for this movie', to='moviecatalog.Genre')),
            ],
        ),
    ]