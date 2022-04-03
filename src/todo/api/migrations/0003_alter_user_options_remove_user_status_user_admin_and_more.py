# Generated by Django 4.0.3 on 2022-04-02 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_user_is_staff_alter_user_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('create_task', 'Create task user'),)},
        ),
        migrations.RemoveField(
            model_name='user',
            name='status',
        ),
        migrations.AddField(
            model_name='user',
            name='ADMIN',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='ROOT_ADMIN',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='WORKERS',
            field=models.BooleanField(default=True),
        ),
    ]