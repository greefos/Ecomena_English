# Generated by Django 4.0.6 on 2022-07-12 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eco', '0003_comment_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
