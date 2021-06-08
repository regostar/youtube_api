# Generated by Django 3.2.4 on 2021-06-08 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('publishing_datetime', models.DateTimeField()),
                ('thumbnails', models.TextField()),
            ],
        ),
    ]