# Generated by Django 3.0.8 on 2020-08-01 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_vaccine_trx_dose_late_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nutrition_master',
            fields=[
                ('n_id', models.AutoField(primary_key=True, serialize=False)),
                ('n_name', models.CharField(max_length=500)),
                ('weight_in_grams_perday', models.FloatField()),
                ('catogory', models.CharField(max_length=500)),
                ('total_duration_in_days', models.IntegerField()),
                ('total_nutrition_alloted_ingrams', models.FloatField()),
            ],
            options={
                'db_table': 'nutrtition_master',
            },
        ),
        migrations.AddField(
            model_name='child_details',
            name='nutrition_days',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='child_details',
            name='nutrition_eligible_from',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='child_details',
            name='nutrition_eligible_till',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pregnant_details',
            name='nutrition_days',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pregnant_details',
            name='nutrition_eligible_from',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pregnant_details',
            name='nutrition_eligible_till',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
    ]
