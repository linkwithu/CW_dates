# Generated by Django 3.2.19 on 2023-06-27 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Work_week',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('MondayGal', models.CharField(choices=[('Kristina', 'Kristina'), ('Lena', 'Lena'), ('Milana', 'Milana'), ('Violetta', 'Violetta'), ('Andrey', 'Andrey'), ('Syun', 'Syun'), ('Inna', 'Inna'), ('Kirill', 'Kirill')], max_length=8)),
                ('TuesdayGal', models.CharField(choices=[('Kristina', 'Kristina'), ('Lena', 'Lena'), ('Milana', 'Milana'), ('Violetta', 'Violetta'), ('Andrey', 'Andrey'), ('Syun', 'Syun'), ('Inna', 'Inna'), ('Kirill', 'Kirill')], max_length=8)),
                ('WednesdayGal', models.CharField(choices=[('Kristina', 'Kristina'), ('Lena', 'Lena'), ('Milana', 'Milana'), ('Violetta', 'Violetta'), ('Andrey', 'Andrey'), ('Syun', 'Syun'), ('Inna', 'Inna'), ('Kirill', 'Kirill')], max_length=8)),
                ('ThursdayGal', models.CharField(choices=[('Kristina', 'Kristina'), ('Lena', 'Lena'), ('Milana', 'Milana'), ('Violetta', 'Violetta'), ('Andrey', 'Andrey'), ('Syun', 'Syun'), ('Inna', 'Inna'), ('Kirill', 'Kirill')], max_length=8)),
                ('FridayGal', models.CharField(choices=[('Kristina', 'Kristina'), ('Lena', 'Lena'), ('Milana', 'Milana'), ('Violetta', 'Violetta'), ('Andrey', 'Andrey'), ('Syun', 'Syun'), ('Inna', 'Inna'), ('Kirill', 'Kirill')], max_length=8)),
                ('SaturdayGal', models.CharField(choices=[('Kristina', 'Kristina'), ('Lena', 'Lena'), ('Milana', 'Milana'), ('Violetta', 'Violetta'), ('Andrey', 'Andrey'), ('Syun', 'Syun'), ('Inna', 'Inna'), ('Kirill', 'Kirill')], max_length=8)),
                ('SundayGal', models.CharField(choices=[('Kristina', 'Kristina'), ('Lena', 'Lena'), ('Milana', 'Milana'), ('Violetta', 'Violetta'), ('Andrey', 'Andrey'), ('Syun', 'Syun'), ('Inna', 'Inna'), ('Kirill', 'Kirill')], max_length=8)),
                ('MondayVos', models.CharField(choices=[('Kristina', 'Kristina'), ('Lena', 'Lena'), ('Milana', 'Milana'), ('Violetta', 'Violetta'), ('Andrey', 'Andrey'), ('Syun', 'Syun'), ('Inna', 'Inna'), ('Kirill', 'Kirill')], max_length=8)),
                ('TuesdayVos', models.CharField(choices=[('Kristina', 'Kristina'), ('Lena', 'Lena'), ('Milana', 'Milana'), ('Violetta', 'Violetta'), ('Andrey', 'Andrey'), ('Syun', 'Syun'), ('Inna', 'Inna'), ('Kirill', 'Kirill')], max_length=8)),
                ('WednesdayVos', models.CharField(choices=[('Kristina', 'Kristina'), ('Lena', 'Lena'), ('Milana', 'Milana'), ('Violetta', 'Violetta'), ('Andrey', 'Andrey'), ('Syun', 'Syun'), ('Inna', 'Inna'), ('Kirill', 'Kirill')], max_length=8)),
                ('ThursdayVos', models.CharField(choices=[('Kristina', 'Kristina'), ('Lena', 'Lena'), ('Milana', 'Milana'), ('Violetta', 'Violetta'), ('Andrey', 'Andrey'), ('Syun', 'Syun'), ('Inna', 'Inna'), ('Kirill', 'Kirill')], max_length=8)),
                ('FridayVos', models.CharField(choices=[('Kristina', 'Kristina'), ('Lena', 'Lena'), ('Milana', 'Milana'), ('Violetta', 'Violetta'), ('Andrey', 'Andrey'), ('Syun', 'Syun'), ('Inna', 'Inna'), ('Kirill', 'Kirill')], max_length=8)),
                ('SaturdayVos', models.CharField(choices=[('Kristina', 'Kristina'), ('Lena', 'Lena'), ('Milana', 'Milana'), ('Violetta', 'Violetta'), ('Andrey', 'Andrey'), ('Syun', 'Syun'), ('Inna', 'Inna'), ('Kirill', 'Kirill')], max_length=8)),
                ('SundayVos', models.CharField(choices=[('Kristina', 'Kristina'), ('Lena', 'Lena'), ('Milana', 'Milana'), ('Violetta', 'Violetta'), ('Andrey', 'Andrey'), ('Syun', 'Syun'), ('Inna', 'Inna'), ('Kirill', 'Kirill')], max_length=8)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
