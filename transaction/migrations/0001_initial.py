# Generated by Django 3.2.4 on 2021-07-10 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('device', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='transaction_model',
            fields=[
                ('txn_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('txn_amt', models.FloatField()),
                ('txn_status', models.CharField(default='none', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(default='No Description Available', max_length=150)),
                ('transaction_type', models.CharField(default='online', max_length=150)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.device')),
            ],
        ),
    ]
