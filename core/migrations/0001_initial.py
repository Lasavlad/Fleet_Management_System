# Generated by Django 4.1.6 on 2023-02-02 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number_1', models.CharField(max_length=10)),
                ('phone_number_2', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
                ('position', models.CharField(max_length=64)),
                ('hiring_date', models.DateField()),
                ('salary', models.PositiveIntegerField()),
                ('is_staff', models.BooleanField()),
                ('driver_id', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Fleet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_in_person', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_1', models.IntegerField()),
                ('phone_2', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=64)),
                ('destination', models.CharField(max_length=64)),
                ('date_of_trip', models.DateField()),
                ('time_of_departure', models.TimeField()),
                ('time_of_arrival', models.TimeField()),
                ('diesel_required', models.IntegerField()),
                ('nature_of_load', models.CharField(max_length=64)),
                ('load_weight', models.IntegerField()),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=64)),
                ('model', models.CharField(max_length=64)),
                ('date_of_production', models.DateField()),
                ('vin_number', models.IntegerField()),
                ('load_capacity', models.IntegerField()),
                ('axle_configuration', models.IntegerField()),
                ('length', models.IntegerField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('assigned_driver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.driver')),
                ('fleet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.fleet')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TripCost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_of_diesel', models.IntegerField()),
                ('revenue_settled', models.IntegerField()),
                ('driver_upkeep', models.IntegerField()),
                ('title', models.CharField(max_length=64)),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('cost', models.IntegerField(default=100)),
                ('receipt', models.FileField(upload_to='')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.trip')),
                ('truck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.truck')),
            ],
        ),
        migrations.AddField(
            model_name='trip',
            name='truck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.truck'),
        ),
        migrations.CreateModel(
            name='Maintainance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintaince_code', models.IntegerField()),
                ('title', models.CharField(max_length=64)),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=64)),
                ('cost', models.IntegerField()),
                ('receipt', models.FileField(upload_to='')),
                ('truck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.truck')),
            ],
        ),
    ]
