# Generated by Django 3.1.7 on 2021-02-25 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20210225_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='color',
            field=models.CharField(choices=[('s', 'success'), ('d', 'danger'), ('w', 'warning'), ('i', 'info'), ('l', 'light')], default='l', max_length=2),
        ),
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('dn', 'Done'), ('nd', 'Not Done')], default='nt', max_length=2),
        ),
    ]
