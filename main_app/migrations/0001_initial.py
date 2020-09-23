# Generated by Django 3.0.8 on 2020-09-23 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('instructions', models.TextField()),
                ('favorite', models.BooleanField(default=False)),
                ('main_ingredient', models.CharField(choices=[('C', 'Chicken'), ('P', 'Pork'), ('B', 'Beef'), ('F', 'Fish'), ('S', 'Shellfish'), ('L', 'Lamb'), ('N', 'Pasta'), ('V', 'Vegetarian'), ('O', 'Other')], default='C', max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='meal date')),
                ('meal_type', models.CharField(choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner')], default='B', max_length=1)),
                ('recipe', models.ManyToManyField(to='main_app.Recipe')),
            ],
        ),
    ]
