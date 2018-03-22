# Generated by Django 2.0.2 on 2018-02-19 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('document', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=100)),
                ('pid', models.CharField(max_length=8)),
                ('hrmax', models.FloatField()),
                ('hrmin', models.FloatField()),
                ('hrmaxmin', models.FloatField()),
                ('hrmean', models.FloatField()),
                ('hrstd', models.FloatField()),
                ('sbpmax', models.FloatField()),
                ('sbpmin', models.FloatField()),
                ('sbpmaxmin', models.FloatField()),
                ('sbpmean', models.FloatField()),
                ('sbpstd', models.FloatField()),
                ('dbpmax', models.FloatField()),
                ('dbpmin', models.FloatField()),
                ('dbpmaxmin', models.FloatField()),
                ('dbpmean', models.FloatField()),
                ('dbpstd', models.FloatField()),
                ('vpmax', models.FloatField()),
                ('vpmin', models.FloatField()),
                ('vpmaxmin', models.FloatField()),
                ('vpmean', models.FloatField()),
                ('vpstd', models.FloatField()),
                ('apmax', models.FloatField()),
                ('apmin', models.FloatField()),
                ('apmaxmin', models.FloatField()),
                ('apmean', models.FloatField()),
                ('apstd', models.FloatField()),
                ('ktvslope', models.FloatField()),
                ('tbvslope', models.FloatField()),
            ],
        ),
    ]
