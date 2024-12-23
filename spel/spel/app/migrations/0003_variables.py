# Generated by Django 5.1.1 on 2024-10-09 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_moduledependency'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('dim', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'variables',
                'managed': False,
            },
        ),
    ]
