# Generated by Django 4.1 on 2022-08-22 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('junimoDatabase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_needed', models.IntegerField()),
                ('blueprint_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='junimoDatabase.blueprint')),
                ('resource_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='junimoDatabase.resource')),
            ],
        ),
    ]