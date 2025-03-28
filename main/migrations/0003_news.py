# Generated by Django 5.1.5 on 2025-03-11 15:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('popularity', models.BooleanField(default=False)),
                ('img1', models.ImageField(blank=True, null=True, upload_to='upload')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='upload')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.subject')),
            ],
        ),
    ]
