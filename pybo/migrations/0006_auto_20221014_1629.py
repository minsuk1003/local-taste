# Generated by Django 3.1.13 on 2022-10-14 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0005_answer_voter_question_voter_alter_answer_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField()),
                ('review', models.CharField(blank=True, max_length=1000, null=True)),
                ('user_name', models.CharField(max_length=50)),
                ('local_review_count', models.IntegerField(blank=True, null=True)),
                ('total_review_count', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'rating',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('restaurant_num', models.AutoField(primary_key=True, serialize=False)),
                ('restaurant_name', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
                ('phone_num', models.CharField(blank=True, max_length=15, null=True)),
                ('type', models.CharField(blank=True, max_length=30, null=True)),
                ('business_hour', models.CharField(blank=True, max_length=50, null=True)),
                ('holiday', models.CharField(blank=True, max_length=10, null=True)),
                ('average_rating', models.DecimalField(blank=True, decimal_places=1, max_digits=1, null=True)),
                ('review_count', models.PositiveIntegerField(blank=True, null=True)),
                ('image_link', models.CharField(blank=True, max_length=3000, null=True)),
            ],
            options={
                'db_table': 'restaurant',
                'managed': False,
            },
        ),
        migrations.AlterField(
            model_name='answer',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
