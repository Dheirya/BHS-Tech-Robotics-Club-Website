# Generated by Django 5.2 on 2025-05-19 13:24

import django.db.models.deletion
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TechApp', '0030_alter_comment_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(help_text='Content of the comment', max_length=300),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Date and time of the comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, help_text='IP address of the commenter', null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(help_text='Name of the commenter', max_length=32),
        ),
        migrations.AlterField(
            model_name='comment',
            name='project',
            field=models.ForeignKey(help_text='Project related to the comment', on_delete=django.db.models.deletion.CASCADE, to='TechApp.project'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(help_text='Upload an image', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(help_text='Title of the image', max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='blurb',
            field=models.TextField(help_text='Short description of the project', max_length=750),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=tinymce.models.HTMLField(help_text='Detailed description of the project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='images',
            field=models.ManyToManyField(help_text='Images related to the project', to='TechApp.image'),
        ),
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, help_text='External link to the project', null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(help_text='Title of the project', max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='topic',
            field=models.ForeignKey(help_text='Topic related to the project', on_delete=django.db.models.deletion.CASCADE, to='TechApp.topic'),
        ),
        migrations.AlterField(
            model_name='projectupdate',
            name='date',
            field=models.DateTimeField(auto_now_add=True, help_text='Date of the update'),
        ),
        migrations.AlterField(
            model_name='projectupdate',
            name='project',
            field=models.ForeignKey(help_text='Project related to the update', on_delete=django.db.models.deletion.CASCADE, to='TechApp.project'),
        ),
        migrations.AlterField(
            model_name='projectupdate',
            name='updateDescription',
            field=models.TextField(help_text='Description of the update'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='coverImage',
            field=models.ForeignKey(help_text='Cover image for the topic', on_delete=django.db.models.deletion.CASCADE, to='TechApp.image'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=models.TextField(help_text='Description of the topic'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(help_text='Title of the topic', max_length=250, unique=True),
        ),
    ]
