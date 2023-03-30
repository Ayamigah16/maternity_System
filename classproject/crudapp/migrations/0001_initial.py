# Generated by Django 4.1.4 on 2023-03-19 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('doctor_id', models.IntegerField(primary_key=True, serialize=False)),
                ('doc_name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=15)),
                ('speciality', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'doctor',
            },
        ),
        migrations.CreateModel(
            name='Neonatal_care',
            fields=[
                ('baby_id', models.IntegerField(primary_key=True, serialize=False)),
                ('birth_date', models.DateTimeField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('length', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'db_table': 'neonatal_care',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('patient_name', models.CharField(max_length=50)),
                ('patient_contact', models.CharField(max_length=200)),
                ('med_history', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'patient',
            },
        ),
        migrations.CreateModel(
            name='Obstetric_care',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_date', models.DateTimeField()),
                ('delivery_date', models.DateTimeField()),
                ('medi_interventions', models.CharField(max_length=200)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='obs_care', to='crudapp.patient')),
            ],
            options={
                'db_table': 'obstetric_care',
            },
        ),
        migrations.CreateModel(
            name='Meidical_Records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis', models.CharField(max_length=200)),
                ('treatment_plan', models.CharField(max_length=200)),
                ('medication', models.CharField(max_length=200)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicals', to='crudapp.patient')),
            ],
            options={
                'db_table': 'medical_records',
            },
        ),
        migrations.CreateModel(
            name='Billings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_owned', models.DecimalField(decimal_places=2, max_digits=5)),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=5)),
                ('insurance_info', models.CharField(max_length=200)),
                ('payment_date', models.DateTimeField()),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bills', to='crudapp.patient')),
            ],
            options={
                'db_table': 'billings',
            },
        ),
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('appointment_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('appointment_date', models.DateTimeField()),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='docToMeet', to='crudapp.doctors')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment', to='crudapp.patient')),
            ],
            options={
                'db_table': 'appointments',
            },
        ),
    ]
