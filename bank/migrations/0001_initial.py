# Generated by Django 3.2.5 on 2021-08-10 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('currentbalance', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='transferhistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=122)),
                ('receiver', models.CharField(max_length=122)),
                ('amount', models.CharField(max_length=122)),
                ('semail', models.CharField(blank=True, max_length=122, null=True)),
                ('remail', models.CharField(blank=True, max_length=122, null=True)),
            ],
        ),
    ]
