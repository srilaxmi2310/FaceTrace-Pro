# Generated by Django 5.0.1 on 2024-03-26 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('is_police', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MissingPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('address', models.TextField()),
                ('aadhar_number', models.CharField(max_length=12, unique=True)),
                ('image', models.ImageField(upload_to='missing_persons/')),
                ('missing_from', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=10)),
                ('location', models.CharField(max_length=255)),
                ('reported_by', models.CharField(max_length=255)),
                ('investigating_police', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Police',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_id', models.CharField(max_length=255)),
                ('policestation', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('phnnum', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_id', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('phn_num', models.CharField(max_length=255)),
            ],
        ),
    ]