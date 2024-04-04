# Generated by Django 5.0.3 on 2024-04-04 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('type_of_request', models.CharField(choices=[('Gas Leak', 'Gas Leak'), ('Meter Reading', 'Meter Reading'), ('Connection Issue', 'Connection Issue')], max_length=100)),
                ('details', models.TextField()),
                ('attachment', models.FileField(blank=True, null=True, upload_to='attachments/')),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('resolved_at', models.DateTimeField(blank=True, null=True)),
                ('pending', models.BooleanField(default=True)),
                ('resolved', models.BooleanField(default=False)),
            ],
        ),
    ]
