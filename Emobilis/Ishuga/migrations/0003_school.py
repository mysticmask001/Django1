# Generated by Django 5.0.2 on 2024-02-26 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ishuga', '0002_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('Location', models.CharField(max_length=20)),
            ],
        ),
    ]