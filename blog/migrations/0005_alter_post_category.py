# Generated by Django 4.2.3 on 2023-07-19 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('HTML/CSS', 'HTML/CSS'), ('Python', 'Python'), ('Django', 'Django'), ('고양이', '고양이')], max_length=50),
        ),
    ]