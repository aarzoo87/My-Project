# Generated by Django 4.2.2 on 2024-04-21 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_login_table_usertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='owner_cancel',
            field=models.CharField(default='No', max_length=255),
        ),
        migrations.AlterField(
            model_name='login_table',
            name='usertype',
            field=models.CharField(choices=[('Lessor', 'Lessor'), ('Lessee', 'Lessee')], max_length=100),
        ),
    ]
