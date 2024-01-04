# Generated by Django 3.2 on 2024-01-04 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('summary', models.TextField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='InputText',
        ),
    ]
