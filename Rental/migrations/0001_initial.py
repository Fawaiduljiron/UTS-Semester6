# Generated by Django 5.0.3 on 2024-05-08 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keuangan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pemesanan', models.CharField(max_length=255)),
                ('total_pembayaran', models.DecimalField(decimal_places=2, max_digits=10)),
                ('metode_pembayaran', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Mobil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis_mobil', models.CharField(max_length=255)),
                ('lokasi', models.CharField(max_length=255)),
                ('tersedia', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pemesanan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_pemesan', models.CharField(max_length=255)),
                ('mobil', models.CharField(max_length=255)),
                ('tanggal_pemesanan', models.DateField()),
            ],
        ),
    ]
