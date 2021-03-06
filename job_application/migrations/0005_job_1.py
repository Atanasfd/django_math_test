# Generated by Django 2.0.1 on 2018-05-29 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('job_application', '0004_delete_job_1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstQuestion', models.CharField(max_length=800, verbose_name='Tell us about yourself.')),
                ('secondQuestion', models.FloatField(max_length=2, verbose_name='How much experience do you have is similar positions?')),
                ('thirdQuestion', models.FloatField(max_length=5, verbose_name='What are your salary expectations?')),
                ('fourthQuestion', models.CharField(max_length=600, verbose_name='What are your strengths and weaknesses?')),
                ('fifthQuestion', models.CharField(max_length=100, verbose_name='When can you start?')),
            ],
        ),
    ]
