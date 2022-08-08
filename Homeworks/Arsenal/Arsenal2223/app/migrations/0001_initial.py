# Generated by Django 4.0.6 on 2022-07-29 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('backnumber', models.CharField(max_length=2)),
                ('position', models.CharField(choices=[('FW', 'Forward'), ('MF', 'Midfielder'), ('DF', 'Defender'), ('GK', 'Goalkeeper')], max_length=2)),
                ('age', models.CharField(max_length=2)),
                ('nationality', models.CharField(max_length=200)),
                ('foot', models.CharField(choices=[('R', 'Right'), ('L', 'Left'), ('Both', 'Both')], max_length=4)),
            ],
        ),
    ]
