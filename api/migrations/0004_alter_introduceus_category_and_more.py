# Generated by Django 4.0.3 on 2022-04-08 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_introduceus_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='introduceus',
            name='category',
            field=models.CharField(choices=[('Professor', 'Professor'), ('MS Students', 'MS Students'), ('Research Collaborators', 'Research Collaborators'), ('PhD Students', 'PhD Students'), ('Research Professor', 'Research Professor'), ('Undergraduate', 'Undergraduate')], max_length=40),
        ),
        migrations.AlterField(
            model_name='publicationsyears',
            name='year',
            field=models.CharField(choices=[('2022', 2022), ('2021', 2021), ('2023', 2023), ('2016', 2016), ('2017', 2017), ('2018', 2018), ('2015', 2015), ('2020', 2020), ('2019', 2019)], max_length=30, unique=True),
        ),
    ]