# Generated by Django 3.1 on 2020-08-23 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Mineral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('elements', models.ManyToManyField(to='minerals.Element')),
                ('items', models.ManyToManyField(to='minerals.Item')),
                ('materials', models.ManyToManyField(to='minerals.Material')),
            ],
        ),
        migrations.CreateModel(
            name='MineralUses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('mineral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minerals.mineral')),
            ],
        ),
        migrations.CreateModel(
            name='ElementUses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('mineral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minerals.mineral')),
            ],
        ),
        migrations.AddField(
            model_name='element',
            name='items',
            field=models.ManyToManyField(to='minerals.Item'),
        ),
        migrations.AddField(
            model_name='element',
            name='materials',
            field=models.ManyToManyField(to='minerals.Material'),
        ),
    ]
