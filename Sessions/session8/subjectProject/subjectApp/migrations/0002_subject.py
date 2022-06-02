# Generated by Django 4.0.3 on 2022-04-07 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjectApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('professor', models.CharField(max_length=100)),
                ('Memo', models.CharField(max_length=100)),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='subjectApp.major')),
            ],
        ),
    ]