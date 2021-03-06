# Generated by Django 2.1 on 2020-04-21 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('Category', models.ManyToManyField(related_name='categories', to='organizations.Category')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationBranch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='locations.Location')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='branches', to='organizations.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='organization',
            name='products_services',
            field=models.ManyToManyField(related_name='products', to='organizations.Product'),
        ),
        migrations.AddField(
            model_name='contact',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='contacts', to='organizations.Organization'),
        ),
        migrations.AddField(
            model_name='contact',
            name='organization_branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.OrganizationBranch'),
        ),
    ]
